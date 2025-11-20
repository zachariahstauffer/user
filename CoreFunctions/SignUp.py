from CoreFunctions.Data import Data
from CoreFunctions.Verify import Verify
import bcrypt

class Sign_up:
    def __init__(self):
        self.data = Data()
    
    def sign_up(self,  username, password):
        
        hashed_password = self.text_to_hash(password)

        val, list_of_flags = Verify().verify_sign_up(username, password)

        if not val:
            return val, list_of_flags
        
        self.data.save(username, hashed_password)
        return val, ['Sign up successfull']
    

    def text_to_hash(self, password):
        password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password, salt)