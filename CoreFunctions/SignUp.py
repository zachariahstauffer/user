from CoreFunctions.Data import Data
from CoreFunctions.Verify import Verify
from CoreFunctions.User import User

class Sign_up:
    def __init__(self):
        self.data = Data()
    
    def sign_up(self,  username, password):
        new_user = User(username, password)
        val, list_of_flags = Verify().verify_sign_up(username, password)

        if not val:
            return val, list_of_flags
        
        self.data.save(new_user)
        return val, ['Sign up successfull']