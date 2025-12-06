import random
import string
import time

from CoreFunctions.SignUp import SignUpClass
from CoreFunctions.Login import LoginClass
from CoreFunctions.Data import DataClass

signup = SignUpClass()
login = LoginClass()
data = DataClass()

def random_username():
    letters = string.ascii_lowercase

    while True:
        name = ""
        for i in range(10):
            name += random.choice(letters)

        exists = data.check_for_existing_user(name)

        if not exists:
            return name


def random_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&"
    chars = letters + numbers + symbols

    pw = ""
    for i in range(10):
        pw += random.choice(chars)

    return pw


def create_users(n):
    print("Creating", n, "users...\n")
    users = []

    for i in range(n):
        u = random_username()
        p = random_password()

        ok, msg_list = signup.sign_up(u, p)

        print("SIGNUP:", u)
        for m in msg_list:
            print("  ->", m)

        if ok:
            print("  STATUS: SUCCESS\n")
            users.append((u, p))
        else:
            print("  STATUS: FAILED\n")

    return users


def login_users(users):
    print("Attempting to login all created users...\n")
    logged_in = []

    for u, p in users:
        msg_list, correct, user_obj = login.login(u, p)

        print("LOGIN:", u)
        for m in msg_list:
            print("  ->", m)

        if correct and user_obj is not None:
            print("  STATUS: SUCCESS\n")
            logged_in.append((u, user_obj))
        else:
            print("  STATUS: FAILED\n")

    return logged_in


def delete_some(logged_in):
    print("Deleting 1/3 of logged-in users...\n")

    if len(logged_in) == 0:
        print("  No logged-in users to delete.\n")
        return logged_in

    amount = max(1, len(logged_in) // 3)
    to_delete = random.sample(logged_in, amount)

    for u, obj in to_delete:
        user_id = obj.get_user_id()
        print("DELETING:", u, "(ID:", user_id, ")")
        data.delete_user(user_id)

    print()
    return [pair for pair in logged_in if pair not in to_delete]


def stress_cycle():
    users = create_users(10)
    logged_in = login_users(users)
    logged_in = delete_some(logged_in)

    print("Creating 5 more users after deletion...\n")
    create_users(5)

    print("Re-login original batch (some will fail if deleted)...\n")
    login_users(users)


def run_stress_test(cycles):
    for i in range(cycles):
        print("\n===============================")
        print("========== CYCLE", i + 1, "==========")
        print("===============================\n")

        stress_cycle()
        time.sleep(0.5)


if __name__ == "__main__":
    run_stress_test(30)
