# StressTest.py

import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

from CoreFunctions import SignUpClass
from CoreFunctions import LoginClass
from CoreFunctions import DataClass
from CoreFunctions import UserClass  # assuming this is exported too


class StressTest:
    def __init__(self, total_users=5000, max_workers=None):
        """
        total_users: how many logical 'tasks' to run (not all will be unique users,
                     because some scenarios reuse usernames).
        max_workers: thread pool size; if None, concurrent.futures uses its default.
        """
        self.total_users = total_users
        self.max_workers = max_workers
        self.signup = SignUpClass()
        self.login = LoginClass()
        self.data = DataClass()

    # ---------- helpers ----------

    def _valid_password(self, idx: int) -> str:
        # Meets your VerifyClass rules: >=6, <=20, upper, lower, digit, special, no spaces
        return f"Abc!{idx}9"

    def _invalid_password_no_upper(self) -> str:
        # No uppercase
        return "abc!19"

    def _invalid_password_too_short(self) -> str:
        # < 6 chars
        return "A!1a"

    # ---------- scenarios ----------

    def _scenario_valid_signup_and_login(self, idx: int):
        username = f"valid_user_{idx}"
        password = self._valid_password(idx)

        ok, flags = self.signup.sign_up(username, password)
        messages, correct, user = self.login.login(username, password)

        # Optional: change password to hit that path, then re-login
        new_password = self._valid_password(idx + 1000000)
        change_msg = ""
        relogin_ok = False

        if user is not None:
            change_msg = user.change_password(new_password)
            _, relogin_ok, _ = self.login.login(username, new_password)

        return {
            "type": "valid_signup_login",
            "signup_ok": ok,
            "signup_flags": flags,
            "login_ok": correct,
            "login_messages": messages,
            "change_password_message": change_msg,
            "relogin_ok_after_change": relogin_ok,
        }

    def _scenario_invalid_signup(self, idx: int):
        username = f"invalid_user_{idx}"

        # Randomly pick one invalid pattern
        if random.random() < 0.5:
            password = self._invalid_password_no_upper()
        else:
            password = self._invalid_password_too_short()

        ok, flags = self.signup.sign_up(username, password)

        return {
            "type": "invalid_signup",
            "signup_ok": ok,
            "signup_flags": flags,  # should contain password errors
        }

    def _scenario_duplicate_signup(self, idx: int):
        username = f"dupe_user_{idx}"
        password = self._valid_password(idx)

        first_ok, first_flags = self.signup.sign_up(username, password)
        second_ok, second_flags = self.signup.sign_up(username, password)

        return {
            "type": "duplicate_signup",
            "first_ok": first_ok,
            "first_flags": first_flags,
            "second_ok": second_ok,          # should be False if user exists
            "second_flags": second_flags,    # should include 'user already exists'
        }

    def _scenario_wrong_password_login(self, idx: int):
        username = f"wrongpass_user_{idx}"
        password = self._valid_password(idx)

        # Ensure the user exists
        self.signup.sign_up(username, password)

        # Correct login
        msgs_ok, correct_ok, user_ok = self.login.login(username, password)
        # Wrong password login
        msgs_bad, correct_bad, user_bad = self.login.login(username, "WrongPass1!")

        return {
            "type": "wrong_password_login",
            "initial_login_ok": correct_ok,
            "initial_login_messages": msgs_ok,
            "wrong_login_ok": correct_bad,        # should be False
            "wrong_login_messages": msgs_bad,
        }

    def _scenario_nonexistent_login(self, idx: int):
        username = f"nonexistent_{idx}"
        msgs, correct, user = self.login.login(username, "Abc!19x")

        return {
            "type": "nonexistent_login",
            "login_ok": correct,      # should be False
            "login_messages": msgs,
            "user_obj": user,         # should be None
        }

    # ---------- task dispatcher ----------

    def _run_one_task(self, idx: int):
        """
        Pick a scenario at random and run it.
        """
        r = random.random()
        if r < 0.30:
            return self._scenario_valid_signup_and_login(idx)
        elif r < 0.50:
            return self._scenario_invalid_signup(idx)
        elif r < 0.70:
            return self._scenario_duplicate_signup(idx)
        elif r < 0.85:
            return self._scenario_wrong_password_login(idx)
        else:
            return self._scenario_nonexistent_login(idx)

    # ---------- public runner ----------

    def run(self):
        # Optional: wipe out all non-admin users before starting
        self.data.wipe()

        print(f"Starting stress test with {self.total_users} tasks...")
        start = time.time()

        results = []

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self._run_one_task, i): i for i in range(self.total_users)}

            for future in as_completed(futures):
                idx = futures[future]
                try:
                    res = future.result()
                    results.append(res)
                except Exception as e:
                    # Collect errors instead of crashing the whole run
                    results.append({
                        "type": "exception",
                        "index": idx,
                        "error": repr(e),
                    })

        elapsed = time.time() - start
        print(f"Stress test finished in {elapsed:.2f} seconds")

        # ---------- basic aggregation / sanity checks ----------

        summary = {
            "valid_signup_login": 0,
            "invalid_signup": 0,
            "duplicate_signup": 0,
            "wrong_password_login": 0,
            "nonexistent_login": 0,
            "exception": 0,
        }

        valid_login_success = 0
        relogin_after_change_success = 0
        invalid_signup_rejected = 0
        duplicate_second_rejected = 0
        wrong_login_rejected = 0
        nonexistent_login_rejected = 0

        for r in results:
            t = r.get("type")
            if t in summary:
                summary[t] += 1

            if t == "valid_signup_login":
                if r.get("signup_ok") and r.get("login_ok"):
                    valid_login_success += 1
                if r.get("relogin_ok_after_change"):
                    relogin_after_change_success += 1

            elif t == "invalid_signup":
                if not r.get("signup_ok"):
                    invalid_signup_rejected += 1

            elif t == "duplicate_signup":
                if r.get("first_ok") and not r.get("second_ok"):
                    duplicate_second_rejected += 1

            elif t == "wrong_password_login":
                if r.get("initial_login_ok") and not r.get("wrong_login_ok"):
                    wrong_login_rejected += 1

            elif t == "nonexistent_login":
                if not r.get("login_ok"):
                    nonexistent_login_rejected += 1

        print("\nScenario counts:")
        for k, v in summary.items():
            print(f"  {k}: {v}")

        print("\nKey correctness checks:")
        print(f"  Valid signup+login success: {valid_login_success}")
        print(f"  Re-login after password change success: {relogin_after_change_success}")
        print(f"  Invalid signups correctly rejected: {invalid_signup_rejected}")
        print(f"  Duplicate second signups rejected: {duplicate_second_rejected}")
        print(f"  Wrong-password logins rejected: {wrong_login_rejected}")
        print(f"  Nonexistent-user logins rejected: {nonexistent_login_rejected}")

        print(f"\nUsers currently in DB: {len(self.data.load_all_users())}")

        return results


if __name__ == "__main__":
    # Adjust these as needed
    TOTAL_USERS = 5000      # number of tasks / operations
    MAX_WORKERS = None      # None = use library default thread count

    tester = StressTest(total_users=TOTAL_USERS, max_workers=MAX_WORKERS)
    tester.run()