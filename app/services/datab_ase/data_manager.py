import sqlite3
from pymongo import MongoClient
import os
import datetime

class SqliteClass:
    def __init__(self):
        self.directory = 'data_folder'
        self.make_dir()
        self.create_table()

    def make_dir(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def create_table(self):
        with sqlite3.connect(f'{self.directory}/data.db') as con:
            cur = con.cursor()
            cur.execute('PRAGMA journal_mode = WAL')
            cur.execute('PRAGMA synchronous = NORMAL')
            cur.execute('PRAGMA busy_timeout = 5000')

            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                admin BOOLEAN,
                username TEXT UNIQUE,
                password_hash BLOB)
                """)
            con.commit()

    def save(self, id,  username, hashed_password):

        with sqlite3.connect(f'{self.directory}/data.db') as file:
            cur = file.cursor()

            cur.execute("""
                INSERT INTO users (id, admin, username, password_hash)
                VALUES (?, ?, ?, ?)
                """, (id, False, username, hashed_password))
            file.commit()
            
    def load(self, user):
        with sqlite3.connect(f'{self.directory}/data.db') as con:
            cur = con.cursor()

            cur.execute("SELECT id, admin, password_hash FROM users WHERE username = ?", (user,))
            row = cur.fetchone()

        if row is None:
            return None, None, None
        
        id, admin, val = row

        return id, admin, val

    def check_for_existing_user(self, username):
        with sqlite3.connect(f'{self.directory}/data.db') as con:
            cur = con.cursor()

            cur.execute("SELECT EXISTS(SELECT 1 FROM users WHERE username = ?)", (username,))

            val = bool(cur.fetchone()[0])

        if val:
            return True

        return False

    def load_all_users(self):
        with sqlite3.connect(f'{self.directory}/data.db') as con:
            cur = con.cursor()

            cur.execute("SELECT * FROM users")

            rows = cur.fetchall()

        return rows

    def delete_user(self, id):
        with sqlite3.connect(f'{self.directory}/data.db') as con:
            cur = con.cursor()
            cur.execute("DELETE FROM users WHERE id = ?", (id,))
            con.commit()
        
    def change_password(self, id, new_hash):
        with sqlite3.connect(f'{self.directory}/data.db') as con:
            cur = con.cursor()

            cur.execute("""
                        UPDATE users 
                        SET password_hash = ? 
                        WHERE id = ?
                        """, (new_hash, id))
            con.commit()

    def change_admin_status(self, id, status):

        with sqlite3.connect(f'{self.directory}/data.db') as con:
            cur = con.cursor()

            cur.execute("""
                        UPDATE users
                        SET admin = ?
                        WHERE id = ?
                        """, (status, id))
            
            con.commit()

    def wipe(self):
        with sqlite3.connect(f'{self.directory}/data.db') as con:
            cur = con.cursor()
            cur.execute("DELETE FROM users WHERE admin <> ?", (True,))
            con.commit()

class MongoDBClass:
    def __init__(self, connection="mongodb://localhost:27017"):
        self.client = MongoClient(connection)
        self.db = self.client['messages']
        self.posts = self.db['posts']

    def store_message(self, sender_id, recipient_id,content):
            

        doc = {
            "sender_id": sender_id,
            "content": content,
            "recipient_id": recipient_id,
            "timestamp": datetime.datetime.now(),
        }

        return str(self.posts.insert_one(doc).inserted_id)
            

    def get_messages(self, message_id):
        return self.posts.find_one({"_id": message_id})

    def get_all_post(self, userID, limit):
        return list(self.posts.find({
            "$or": [
                {"author_id": userID},
                {"recipient_id": userID}
            ]
        }).sort("timestamp", -1).limit(limit))

