from CoreFunctions.Verify import Verify

class Login:
    def __init__(self):
        pass

    def login(self, username, password):

        message = []

        exists, correct = Verify().verify_login(username, password)

        if not exists:
            message.append(f'{username} does not have an account')
            return message, correct
        
        message.append(f'{username} was found')
        
        if correct:
            message.append(f'{username} has logged in')
            return message, correct
        
        message.append('wrong password')

        
        return message, correct