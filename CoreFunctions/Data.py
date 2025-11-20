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
                username TEXT,
                password_hash BLOB)
                """)
            con.commit()

    def save(self, username, hashed_password):


        with sqlite3.connect('data.db') as file:
            cur = file.cursor()

            cur.execute("""
                INSERT INTO users (username, password_hash)
                VALUES (?, ?)
                """, (username, hashed_password))
            file.commit()
            
    def load(self, user):
        with sqlite3.connect('data.db') as con:
            cur = con.cursor()

            cur.execute("SELECT id, password_hash FROM users WHERE username = ?", (user,))
            row = cur.fetchone()

        if row is None:
            return None, None
        
        id, val = row

        return id, val

    def check_for_existing_user(self, username):
        with sqlite3.connect('data.db') as con:
            cur = con.cursor()

            cur.execute("SELECT EXISTS(SELECT 1 FROM users WHERE username = ?)", (username,))

            val = bool(cur.fetchone()[0])

        if val:
            return True

        return False

    def delete_user(self, username):
        with sqlite3.connect('data.db') as con:
            cur = con.cursor()
            cur.execute("DELETE FROM users WHERE username = ?", (username,))
            con.commit()

    def admin(self, username, password):
        with sqlite3.connect('data.db') as con:

            cur = con.cursor()
            # cur.execute('''INSERT INTO users (id, username, password_hash) VALUES (?, ?, ?)''', (0, username, password,))
            cur.execute('SELECT username, password_hash FROM users WHERE id = ?', (0, )) 
            row = cur.fetchone()

            username, password = row

            return username, password
        
    def wipe(self):
        with sqlite3.connect('data.db') as con:
            cur = con.cursor()
            cur.execute("DELETE FROM users WHERE id <> ?", (0,))
            con.commit()
