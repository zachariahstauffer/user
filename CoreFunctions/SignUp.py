from .Data import DataClass
from .Verify import VerifyClass
import bcrypt

class SignUpClass:
    def __init__(self):
        self.data = DataClass()
        self.verify = VerifyClass()
    
    def sign_up(self,  username, password):
        messages, passed = self.verify.verify_sign_up(username, password)

        if not passed:
            return messages, passed
        
        password_hashed = self.text_to_hash(password)
        self.data.save(username, password_hashed)
        return messages, passed

    def text_to_hash(self, password):
        password = password.encode('utf-8')
        salt = bcrypt.gensalt(10)
        return bcrypt.hashpw(password, salt)