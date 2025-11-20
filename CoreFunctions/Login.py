from CoreFunctions.Verify import Verify
from CoreFunctions.Data import Data
from CoreFunctions.User import User

class Login:
    def __init__(self):
        self.verify = Verify()
        self.data = Data()

    def login(self, username, password):

        message = []

        id, hashed_password = self.data.load(username)

        

        exists, correct = self.verify.verify_login(username, password, hashed_password)

        if not exists:
            message.append(f'{username} does not have an account')
            return message, correct, None
        
        message.append(f'{username} was found')
        
        if correct:
            user = User(username, id)
            message.append(f'{username} has logged in')
            return message, correct, user
        
        message.append('wrong password')

        
        return message, correct, None