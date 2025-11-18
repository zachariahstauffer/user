import bcrypt
from CoreFunctions.Data import Data

class Verify:
    def __init__(self):
        self.data = Data()

    def verify_sign_up(self, username, password):
        val = True
        user_exists = False
        list_of_flags = []
        has_upper = has_lower = has_special = has_number = has_space = False

        user_exists = str(self.data.check_for_existing_user(username)).lower()

        if user_exists:
            list_of_flags.append('user already exists')
            val = False

        if len(password) < 6:
            list_of_flags.append('password must be 6 characters long')
            val = False

        if len(password) > 20:
            list_of_flags.append('password can not be more than 20 characters long')
            val = False
        
        for char in password:
            has_upper, has_lower, has_special, has_number, has_space = self.requirements(char, has_upper, has_lower, has_special, has_number, has_space)
        
        if not has_upper:
            list_of_flags.append('password must contain at least one uppercase letter')
            val = False

        if not has_lower:
            list_of_flags.append('password must contain at least one lowercase letter')
            val = False

        if not has_number:
            list_of_flags.append('password must contain at least one number')
            val = False

        if not has_special:
            list_of_flags.append("password must contain at least one special character ['!' , '@', '#', '$', '%', '^', '&']")
            val = False

        if not has_space:
            list_of_flags.append('cannot contain spaces')
            val = False

        return val, list_of_flags

    def requirements(self, char, has_upper, has_lower, has_special, has_number, has_space):
        special = {'!' , '@', "#", '$', '%', '^', '&'}

        if 20 != ord(char):
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

    def verify_login(self,username, password):
        password = password.encode('utf-8')
        hashed = self.data.load(username)
        
        if hashed is None:
            return False, False
        
        if bcrypt.checkpw(password, hashed):
            return True, True
        

        return True, False