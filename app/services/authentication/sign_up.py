from App.Services.DataBase.DataManager import SqliteClass
from App.Services.Authentication.Verify import VerifyClass

import bcrypt
from uuid import uuid4

class SignUpClass:
    def __init__(self):
        self.data = SqliteClass()
        self.verify = VerifyClass()

    def sign_up(self, username, password):
        messages = []
        passed = True

        messages, passed = self.verify.verify_sign_up(username, str(password))

        if not passed:
            return messages, passed
        
        hashed_password = self.password_to_hash(password)
        
        id = str(uuid4())

        self.data.save(id, username, hashed_password)

        if len(messages) == 0:
            messages.append(f"{username} has signed up")

        return messages, passed

    def password_to_hash(self, password):
        salt = bcrypt.gensalt(10)
        encoded_password = password.encode('utf-8')
        hashed_password = ""

        hashed_password = bcrypt.hashpw(encoded_password, salt)

        return hashed_password
