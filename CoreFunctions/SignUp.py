from .Data import DataClass
from .Verify import VerifyClass
import bcrypt

class SignUpClass:
    def __init__(self):
        self.data = DataClass()
    
    def sign_up(self,  username, password):
        

        val, messages = VerifyClass().verify_sign_up(username, password)

        if not val:
            return val, messages
        
        hashed_password = self.text_to_hash(password)
        
        self.data.save(username, hashed_password)
        messages.append('Sign up successfull')
        return val, messages
    

    def text_to_hash(self, password):
        password = password.encode('utf-8')
        salt = bcrypt.gensalt(10)
        return bcrypt.hashpw(password, salt)