import bcrypt

class Verify:
    def __init__(self, password):
        self.password = password

    def verify_sign_up(self):
        val = True
        has_upper = has_lower = has_special = has_number = False

        if len(self.password) < 6:
            print('password must be 6 characters long')
            val = False

        if len(self.password) > 20:
            print('password can not be more than 20 characters long')
            val = False
        
        for char in self.password:
            has_upper, has_lower, has_special, has_number = self.requirements(char, has_upper, has_lower, has_special, has_number)
        
        if not has_upper:
            print('password must contain at least one uppercase letter')
            val = False

        if not has_lower:
            print('password must contain at least one lowercase letter')
            val = False

        if not has_number:
            print('password must contain at least one number')
            val = False

        if not has_special:
            print("password must contain at least one special character ['!' , '@', '#', '$', '%', '^', '&']")
            val = False


        return val

    def requirements(self, char, has_upper, has_lower, has_special, has_number):
        special = {'!' , '@', "#", '$', '%', '^', '&'}

        if 48 <= ord(char) <= 57:
            has_number = True
            
        if 65 <= ord(char) <= 90:
            has_upper = True

        if 97 <= ord(char) <= 122:
            has_lower = True

        if char in special:
            has_special = True

        return has_upper, has_lower, has_special, has_number

    def verify_login(self, has):

        return bool(bcrypt.checkpw(self.password, has))