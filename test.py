import sqlite3
from CoreFunctions.Data import Data
import bcrypt
from CoreFunctions.SignUp import Sign_up

"""

Data()

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


# def add_admin():
#     username = 'admin123'
#     password = '321nimda'.encode('utf-8')

#     password = bcrypt.hashpw(password, bcrypt.gensalt())


#     with sqlite3.connect('data.db') as con:
#         cur = con.cursor()
#         cur.execute('''INSERT INTO users (id, username, password_hash) VALUES (?, ?, ?)''', (0, username, password,))


# add_admin()

"""

"""
class toes:
    def __init__(self):
        self.inputs()

    def inputs(self):
        print('''
              1. Login
              2. SignUp''')

        choice = int(input())

        if choice == 1:
            print('logged in')
        elif choice == 2:
            print('signed up')
        else:
            print('error')


toes()
"""



user = ''
password = ''
signup = Sign_up()

for i in range(1, 21):
    user = f'user{i}'
    password = f'Pass!{i}'

    signup.sign_up(user, password)
