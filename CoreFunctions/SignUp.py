from .Data import DataClass
from .Verify import VerifyClass
import bcrypt

class SignUpClass:
    def __init__(self):
        self.data = DataClass()
        self.verify = VerifyClass()

    def sign_up(self, username, password):
        messages = []
        passed = True

        messages, passed = self.verify.verify_sign_up(username, str(password))

        if not passed:
            return messages, passed
        
        hashed_password = self.password_to_hash(password)

        self.data.save(username, hashed_password)

        if len(messages) == 0:
            messages.append(f"{username} has signed up")

        return messages, passed

    def password_to_hash(self, password):
        salt = bcrypt.gensalt(10)
        encoded_password = password.encode('utf-8')
        hashed_password = ""

        hashed_password = bcrypt.hashpw(encoded_password, salt)

        return hashed_password