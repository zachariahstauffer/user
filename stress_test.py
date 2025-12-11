#!/usr/bin/env python3
"""
Lightweight stress test for CoreFunctions modules.

Exercises: SignUp, Login, Data operations (change password, delete, admin toggle, wipe)
Usage: python3 stress_test.py --threads 50 --ops 1000
"""
import argparse
import random
import string
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

from CoreFunctions.SignUp import SignUpClass
from CoreFunctions.Login import LoginClass
from CoreFunctions.Data import DataClass


def rand_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class StressTest:
    def __init__(self, threads=20, ops=1000, seed=None):
        self.threads = threads
        self.ops = ops
        if seed is not None:
            random.seed(seed)

        # Shared helpers (each class uses its own sqlite connections internally)
        self.signup = SignUpClass()
        self.login = LoginClass()
        self.data = DataClass()

        # Stats
        self.lock = threading.Lock()
        self.stats = {
            'signup_success': 0,
            'signup_fail': 0,
            'login_success': 0,
            'login_fail': 0,
            'delete': 0,
            'change_password': 0,
            'admin_toggle': 0,
            'wipe': 0,
            'exceptions': 0,
        }

        # A pool of usernames we will try to use for login/change/delete
        self.known_usernames = []
        # track exception types and samples for diagnosis
        self.exception_types = {}
        self.exception_samples = []

    def _record(self, key, n=1):
        with self.lock:
            self.stats[key] = self.stats.get(key, 0) + n

    def signup_worker(self):
        # sometimes use a new username, sometimes a likely-duplicate
        if random.random() < 0.8:
            username = f"user_{int(time.time()*1000)}_{rand_string(4)}"
        else:
            # pick an existing or random duplicate; if picking existing, unpack tuple
            if self.known_usernames and random.random() < 0.7:
                username, _ = random.choice(self.known_usernames)
            else:
                username = f"dup_{rand_string(6)}"

        password = f"Aa1!{rand_string(6)}"
        try:
            messages, passed = self.signup.sign_up(username, password)
            if passed:
                with self.lock:
                    self.known_usernames.append((username, password))
                self._record('signup_success')
            else:
                self._record('signup_fail')
        except Exception as e:
            # record exception type and a sample traceback for diagnosis
            import traceback
            tname = type(e).__name__
            with self.lock:
                self.exception_types[tname] = self.exception_types.get(tname, 0) + 1
                if len(self.exception_samples) < 10:
                    self.exception_samples.append(traceback.format_exc())
            self._record('exceptions')

    def login_worker(self):
        if not self.known_usernames or random.random() < 0.3:
            # try random non-existing user
            username = f"no_user_{rand_string(6)}"
            password = "wrongPass123!"
        else:
            username, password = random.choice(self.known_usernames)

        try:
            messages, ok, user = self.login.login(username, password)
            if ok and user is not None:
                self._record('login_success')
            else:
                self._record('login_fail')
        except Exception as e:
            import traceback
            tname = type(e).__name__
            with self.lock:
                self.exception_types[tname] = self.exception_types.get(tname, 0) + 1
                if len(self.exception_samples) < 10:
                    self.exception_samples.append(traceback.format_exc())
            self._record('exceptions')

    def change_password_worker(self):
        # pick a known user and change their password
        if not self.known_usernames:
            return self._record('change_password', 0)

        username, old_pass = random.choice(self.known_usernames)
        try:
            id, admin, hashed = self.data.load(username)
            if id is None:
                self._record('change_password', 0)
                return

            new_pass = f"Aa1!{rand_string(7)}"
            new_hash = self.signup.text_to_hash(new_pass)
            self.data.change_password(id, new_hash)
            # update local cache
            with self.lock:
                for i, (u, p) in enumerate(self.known_usernames):
                    if u == username:
                        self.known_usernames[i] = (username, new_pass)
                        break

            self._record('change_password')
        except Exception as e:
            import traceback
            tname = type(e).__name__
            with self.lock:
                self.exception_types[tname] = self.exception_types.get(tname, 0) + 1
                if len(self.exception_samples) < 10:
                    self.exception_samples.append(traceback.format_exc())
            self._record('exceptions')

    def delete_user_worker(self):
        # pick known user and delete
        if not self.known_usernames:
            return self._record('delete', 0)

        username, _ = random.choice(self.known_usernames)
        try:
            id, admin, hashed = self.data.load(username)
            if id is None:
                return
            self.data.delete_user(id)
            with self.lock:
                self.known_usernames = [t for t in self.known_usernames if t[0] != username]
            self._record('delete')
        except Exception as e:
            import traceback
            tname = type(e).__name__
            with self.lock:
                self.exception_types[tname] = self.exception_types.get(tname, 0) + 1
                if len(self.exception_samples) < 10:
                    self.exception_samples.append(traceback.format_exc())
            self._record('exceptions')

    def admin_toggle_worker(self):
        # pick a user and toggle admin flag
        if not self.known_usernames:
            return self._record('admin_toggle', 0)

        username, _ = random.choice(self.known_usernames)
        try:
            id, admin, hashed = self.data.load(username)
            if id is None:
                return
            new_status = not bool(admin)
            self.data.change_admin_status(id, new_status)
            self._record('admin_toggle')
        except Exception as e:
            import traceback
            tname = type(e).__name__
            with self.lock:
                self.exception_types[tname] = self.exception_types.get(tname, 0) + 1
                if len(self.exception_samples) < 10:
                    self.exception_samples.append(traceback.format_exc())
            self._record('exceptions')

    def wipe_worker(self):
        try:
            # Wipe non-admin users
            self.data.wipe()
            # Clear local cache conservatively (we don't know admin states here)
            with self.lock:
                self.known_usernames = []
            self._record('wipe')
        except Exception:
            self._record('exceptions')

    def run(self):
        start = time.time()

        ops = self.ops
        with ThreadPoolExecutor(max_workers=self.threads) as ex:
            futures = []
            for i in range(ops):
                r = random.random()
                # weight operations differently
                if r < 0.35:
                    futures.append(ex.submit(self.signup_worker))
                elif r < 0.7:
                    futures.append(ex.submit(self.login_worker))
                elif r < 0.82:
                    futures.append(ex.submit(self.change_password_worker))
                elif r < 0.9:
                    futures.append(ex.submit(self.admin_toggle_worker))
                elif r < 0.97:
                    futures.append(ex.submit(self.delete_user_worker))
                else:
                    futures.append(ex.submit(self.wipe_worker))

            # wait for completion
            for f in as_completed(futures):
                try:
                    f.result()
                except Exception as e:
                    import traceback
                    tname = type(e).__name__
                    with self.lock:
                        self.exception_types[tname] = self.exception_types.get(tname, 0) + 1
                        if len(self.exception_samples) < 10:
                            self.exception_samples.append(traceback.format_exc())
                    self._record('exceptions')

        duration = time.time() - start
        # Print summary
        print('\nStress test complete')
        print(f'Threads: {self.threads}, Ops: {self.ops}, Time: {duration:.2f}s')
        for k, v in sorted(self.stats.items()):
            print(f'{k}: {v}')
        if self.exception_types:
            print('\nException types:')
            for tname, cnt in sorted(self.exception_types.items(), key=lambda x: -x[1]):
                print(f'  {tname}: {cnt}')
            print('\nSample traces (up to 10):')
            for s in self.exception_samples:
                print('---')
                print(s)


def main():
    parser = argparse.ArgumentParser(description='Stress test CoreFunctions')
    parser.add_argument('--threads', type=int, default=20, help='Number of worker threads')
    parser.add_argument('--ops', type=int, default=1000, help='Total operations to perform')
    parser.add_argument('--seed', type=int, default=None, help='Random seed')

    args = parser.parse_args()

    st = StressTest(threads=args.threads, ops=args.ops, seed=args.seed)
    st.run()


if __name__ == '__main__':
    main()
