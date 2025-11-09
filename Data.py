import pickle
import sqlite3

class Data:
    def __init__(self):
        self.create_table()

    def create_table(self):
        with sqlite3.connect('data.db') as con:
            cur = con.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password_hash TEXT)
                """)

    def save(self, user):
        # with open('data.dat', 'wb') as file:
        #     pickle.dump(users, file)
        username = user.get_username()
        hashed = user.get_hash()

        with sqlite3.connect('data.db') as file:
            cur = file.cursor()

            cur.execute("""
                INSERT INTO users (username, password_hash)
                VALUES (?, ?)
                """, (username, hashed))


            
        pass

    def read(self, user):
        '''try:

            file = open('data.dat', 'rb')
            self.users = pickle.load(file)

        except EOFError:
            self.users = []

        return self.users'''

        

        with sqlite3.connect('data.db') as con:
            cur = con.cursor()



        pass
    
    def wipe(self):
        # with open('data.dat', 'wb') as file:
        #         pickle.dump([], file)

        pass
