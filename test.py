import sqlite3
from CoreFunctions.Data import Data

def list_users():
    # This will return a list of all user rows in the database.
    # Each row will be a tuple like: (id, username, password_hash)

    with sqlite3.connect('data.db') as con:
        cur = con.cursor()

        # select everything from the users table
        cur.execute("SELECT id, username, password_hash FROM users")

        # fetch all rows at once
        rows = cur.fetchall()

        return rows


all = list_users()

for i in all:
    print(i)


Data().wipe()


all = list_users()

for i in all:
    print(i)