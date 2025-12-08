from .Verify import VerifyClass
from .Data import DataClass
from .User import UserClass

class LoginClass:
    def __init__(self):
        self.verify = VerifyClass()
        self.data = DataClass()

    def login(self, username, password):
        message = []
        user = None
        id, status, hashed_password = self.data.load(username)

        exists, correct_password = self.verify.verify_login(password, hashed_password)

        if not exists:
            message.append(f'{username} does not have an account')

            return message, correct_password, user
        
        message.append(f'{username} was found')

        if status:
            is_admin = True

        elif not status:
            is_admin = False
        
        if correct_password:
            user = UserClass(id, username, is_admin)

            message.append(f'{username} has logged in')

            return message, correct_password, user
        
        message.append('wrong password')

        return message, correct_password, user