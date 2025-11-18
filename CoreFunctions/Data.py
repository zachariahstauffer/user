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

    def save(self, user):
        username = user.get_username()
        hashed = user.get_hash()

        with sqlite3.connect('data.db') as file:
            cur = file.cursor()

            cur.execute("""
                INSERT INTO users (username, password_hash)
                VALUES (?, ?)
                """, (username, hashed))
            file.commit()
            
    def load(self, user):
        with sqlite3.connect('data.db') as con:
            cur = con.cursor()

            cur.execute("SELECT password_hash FROM users WHERE username = ?", (user,))
            row = cur.fetchone()

        if row is None:
            return None
        
        val = row[0]
        return val

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

    def wipe(self):
        with sqlite3.connect('data.db') as con:
            cur = con.cursor()
            cur.execute("DELETE FROM users")
            con.commit()
 