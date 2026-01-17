import sqlite3
from pymongo import MongoClient
import datetime

class SqliteClass:
    def __init__(self):
        self.create_table()

    def create_table(self):
        with sqlite3.connect('data.db') as con:
            cur = con.cursor()
            cur.execute('PRAGMA journal_mode = WAL')
            cur.execute('PRAGMA synchronous = NORMAL')
            cur.execute('PRAGMA busy_timeout = 5000')

            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                admin BOOLEAN,
                username TEXT UNIQUE,
                password_hash BLOB)
                """)
            con.commit()

    def save(self, username, hashed_password):

        with sqlite3.connect('data.db') as file:
            cur = file.cursor()

            cur.execute("""
                INSERT INTO users (admin, username, password_hash)
                VALUES (?, ?, ?)
                """, (False, username, hashed_password))
            file.commit()
            
    def load(self, user):
        with sqlite3.connect('data.db') as con:
            cur = con.cursor()

            cur.execute("SELECT id, admin, password_hash FROM users WHERE username = ?", (user,))
            row = cur.fetchone()

        if row is None:
            return None, None, None
        
        id, admin, val = row

        return id, admin, val

    def check_for_existing_user(self, username):
        with sqlite3.connect('data.db') as con:
            cur = con.cursor()

            cur.execute("SELECT EXISTS(SELECT 1 FROM users WHERE username = ?)", (username,))

            val = bool(cur.fetchone()[0])

        if val:
            return True

        return False

    def load_all_users(self):
        with sqlite3.connect('data.db') as con:
            cur = con.cursor()

            cur.execute("SELECT * FROM users")

            rows = cur.fetchall()

        return rows

    def delete_user(self, id):
        with sqlite3.connect('data.db') as con:
            cur = con.cursor()
            cur.execute("DELETE FROM users WHERE id = ?", (id,))
            con.commit()
        
    def change_password(self, id, new_hash):
        with sqlite3.connect('data.db') as con:
            cur = con.cursor()

            cur.execute("""
                        UPDATE users 
                        SET password_hash = ? 
                        WHERE id = ?
                        """, (new_hash, id))
            con.commit()

    def change_admin_status(self, id, status):

        with sqlite3.connect('data.db') as con:
            cur = con.cursor()

            cur.execute("""
                        UPDATE users
                        SET admin = ?
                        WHERE id = ?
                        """, (status, id))
            
            con.commit()

    def wipe(self):
        with sqlite3.connect('data.db') as con:
            cur = con.cursor()
            cur.execute("DELETE FROM users WHERE admin <> ?", (True,))
            con.commit()



class MongoDBClass:
    def __init__(self, connection="monbodb://localhost:"):
        self.client = MongoClient(connection)
        self.db = self.client['zbear']
        self.posts = self.db['posts']

    def store_post(self, author_id, content):
            

        doc = {
            "author_id": author_id,
            "content": content,
            "timestamp": datetime.datetime.now(),
        }

        return str(self.posts.insert_one(doc).inserted_id)
            

    def get_post(self, message_id):
        return self.posts.find_one({"_id": message_id})

    def get_all_post(self, user_id, limit):
        return list(self.posts.find({
            "$or": [
                {"author_id": user_id},
                {"recipient_id": user_id}
            ]
        }).sort("timestamp", -1).limit(limit))
