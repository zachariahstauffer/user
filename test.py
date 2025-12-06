from CoreFunctions.SignUp import SignUpClass
from CoreFunctions.Data import DataClass
import sqlite3
import bcrypt

data = DataClass()



def list_all_users():
    with sqlite3.connect('data.db') as con:
        cur = con.cursor()

        cur.execute('''
            SELECT * FROM users
        ''')

        return cur.fetchall()
    

list = list_all_users()

for i in list:
    print(i)


data.wipe()


"""
signup = Sign_up()

username = ''
password = ''

for i in range(1,101):
    username=f'user{i}'
    password=f'Pass!{i}'
    signup.sign_upClass(username, password)
    print(f'{username} has been created')
"""

"""

username = 'password'
password = 'admin'.encode('utf-8')
salt = bcrypt.gensalt()
password = bcrypt.hashpw(password, salt)

with sqlite3.connect('data.db') as con:
    cur = con.cursor()

    cur.execute('''
                INSERT INTO users (id, username, password_hash) VALUES (?,?,?)
                ''', (0, username, password))
    
    con.commit()
"""