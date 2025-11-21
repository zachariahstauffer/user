from CoreFunctions.Verify import Verify
from CoreFunctions.Data import Data
from CoreFunctions.User import User

class Login:
    def __init__(self):
        self.verify = Verify()
        self.data = Data()

    def login(self, username, password):
        message = []
        user = None
        id, hashed_password = self.data.load(username)

        exists, correct_password, is_admin = self.verify.verify_login(id ,username, password, hashed_password)

        if not exists:
            message.append(f'{username} does not have an account')

            return message, correct_password, user
        
        message.append(f'{username} was found')
        
        if correct_password:
            user = User(id, username, is_admin)

            message.append(f'{username} has logged in')

            return message, correct_password, user
        
        message.append('wrong password')

        return message, correct_password, user