from .Data import DataClass
from .Verify import VerifyClass
import bcrypt

class SignUpClass:
    def __init__(self):
        self.data = DataClass()
    
    def sign_up(self,  username, password):
        

        val, list_of_flags = VerifyClass().verify_sign_up(username, password)

        if not val:
            return val, list_of_flags
        
        hashed_password = self.text_to_hash(password)
        
        self.data.save(username, hashed_password)
        return val, ['Sign up successfull']
    

    def text_to_hash(self, password):
        password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password, salt)