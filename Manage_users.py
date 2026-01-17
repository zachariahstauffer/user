"""Small admin/manage CLI for the Users project.

Features:
- `list`         : lists all users (same format as before)
- `wipe`         : removes all non-admin users
- `create-admin` : create a new admin user with a hashed password

Recommended new filename: `manage_db.py` (more descriptive than `test.py`).
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from getpass import getpass
from typing import Sequence

import bcrypt

from CoreFunctions.DataManager import SqliteClass


DB_PATH = "data.db"


def list_all_users(db_path: str = DB_PATH):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users")
        return cur.fetchall()


def print_all_users(db_path: str = DB_PATH) -> None:
    users = list_all_users(db_path)

    if not users:
        print("No users found")
        return

    output = f"Total Users: {len(users)}\n\n"

    for user in users:
        id_, admin_flag, username, _ = user
        status = "ADMIN" if admin_flag else "user"
        output += f"ID: {id_} | {status} | {username}\n"

    print(output)


def wipe_non_admins(confirm: bool = False, db_path: str = DB_PATH) -> None:
    if not confirm:
        ans = input("This will DELETE all non-admin users. Continue? [y/N]: ")
        if ans.lower() not in ("y", "yes"):
            print("Aborted.")
            return

    SqliteClass().wipe()
    print("Wiped non-admin users.")


def create_admin(username: str | None = None, password: str | None = None, db_path: str = DB_PATH) -> None:
    dc = SqliteClass()  # ensures table exists

    if username is None:
        username = input("Admin username: ")

    # check for existing user
    if dc.check_for_existing_user(username):
        print(f"User '{username}' already exists. Aborting.")
        return

    if password is None:
        password = getpass("Admin password: ")
        password_confirm = getpass("Confirm password: ")
        if password != password_confirm:
            print("Passwords do not match. Aborting.")
            return

    pw_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pw_bytes, salt)

    # insert directly with admin=True
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO users (admin, username, password_hash) VALUES (?, ?, ?)",
            (True, username, hashed),
        )
        con.commit()

    print(f"Admin user '{username}' created.")


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Manage users DB: list, wipe, create-admin")
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("list", help="List all users")

    wipe_p = sub.add_parser("wipe", help="Delete all non-admin users")
    wipe_p.add_argument("--yes", action="store_true", help="Skip confirmation")

    ca_p = sub.add_parser("create-admin", help="Create an admin user")
    ca_p.add_argument("--username", help="Admin username")
    ca_p.add_argument("--password", help="Admin password (unsafe on CLI)")

    # ensure DB and tables exist
    SqliteClass()

    args = p.parse_args(argv)

    if args.cmd == "list":
        print_all_users()
        return 0

    if args.cmd == "wipe":
        wipe_non_admins(confirm=args.yes)
        return 0

    if args.cmd == "create-admin":
        create_admin(username=args.username, password=args.password)
        return 0

    p.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
