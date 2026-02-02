import bcrypt
from .DataManager import SqliteClass

class VerifyClass:
    def __init__(self):
        self.data = SqliteClass()

    def verify_sign_up(self, username, password):
        passed: bool = True
        passed_username: bool = True
        passed_password: bool = True
        username_messages: list = []
        password_messages: list = []
        messages: list = []

        username_messages, passed_username  = self.verify_username(username)
        password_messages, passed_password = self.verify_password(password)

        if not passed_username or not passed_password:
            passed = False
            messages = username_messages + password_messages
            return messages, passed
        
        return messages, passed

    def verify_login(self, password, hashed):
        password = password.encode('utf-8')
        
        if hashed is None:
            return False, False
        
        if bcrypt.checkpw(password, hashed):
            return True, True
        
        return True, False
    
    def verify_username(self, username):
        has_space = has_special = False
        special = {'!' , '@', "#", '$', '%', '^', '&'}
        messages = []
        user_exists = False
        passed = True

        user_exists = self.data.check_for_existing_user(username)

        if user_exists:
            messages.append(f"{username} already exists")
            passed = False

        for char in username:
            if ord(' ') == ord(char):
                has_space = True

            if char in special:
                has_special = True

        if has_space:
            messages.append('Cannot contain spaces')
            passed = False

        if has_special:
            messages.append('Connot contain scpecial characters (!, @, #, $, %, ^, &)')
            passed = False

        return messages, passed

    def verify_password(self, password):

        passed:  bool = True
        messages: list = []

        has_upper = has_lower = has_special = has_number = has_space = False

        if len(password) < 6:
            messages.append('password must be 6 characters long')
            passed = False

        if len(password) > 20:
            messages.append('password can not be more than 20 characters long')
            passed = False
        
        for char in password:
            has_upper, has_lower, has_special, has_number, has_space = self.requirements(char, has_upper, has_lower, has_special, has_number, has_space)
        
        if not has_upper:
            messages.append('password must contain at least one uppercase letter')
            passed = False

        if not has_lower:
            messages.append('password must contain at least one lowercase letter')
            passed = False

        if not has_number:
            messages.append('password must contain at least one number')
            passed = False

        if not has_special:
            messages.append("password must contain at least one special character (!, @, #, $, %, ^, &)")
            passed = False

        if has_space:
            messages.append('password cannot contain spaces')
            passed = False


        return messages, passed

    def requirements(self, char, has_upper, has_lower, has_special, has_number, has_space):
        special = {'!' , '@', "#", '$', '%', '^', '&'}

        if ord(' ') == ord(char):
            has_space = True

        if 48 <= ord(char) <= 57:
            has_number = True
            
        if 65 <= ord(char) <= 90:
            has_upper = True

        if 97 <= ord(char) <= 122:
            has_lower = True

        if char in special:
            has_special = True

        return has_upper, has_lower, has_special, has_number, has_space
