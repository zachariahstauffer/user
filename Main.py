import bcrypt
import pickle

class data:
    def __init__(self,):
        self.users = []

    def save(self, users = []):
        with open('data.dat', 'wb') as file:
            pickle.dump(users, file)

    def read(self):
        try:

            file = open('data.dat', 'rb')
            self.users = pickle.load(file)

        except EOFError:
            self.users = []

        return self.users

class txt_to_hash:
    def __init__(self, tx: str):
        self.tx = tx
        self.s = bcrypt.gensalt()
        self.en = tx.encode('utf-8')
    
    def hashh(self):

        return bcrypt.hashpw(self.en, self.s)

class user:
    def __init__(self, username: str, password):
        self.username = username
        self.has = b''
        self.hass(password)
    
    def get_username(self):
        return self.username
    
    def hass(self, password):
        self.has = txt_to_hash(password).hashh()

    def get_has(self):
        return self.has
    
class verify:
    def __init__(self, password):
        self.password = password

    def vs(self):
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

        if has_upper and has_lower and has_special and has_upper:
            return val
        
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

    def vl(self, has):

        return bool(bcrypt.checkpw(self.password, has))
    
class display:
    def __init__(self):
        self.users = []
        self.data = data()
        self.check_data()

    def sign_up(self):
        username = str(input("Make Username: "))
        password = str(input("Make Password: "))

        new_user = user(username, password)

        if verify(password).vs():
            self.users.append(new_user)
        
        self.data.save(self.users)

    def login(self):
        username = str(input("Username: "))
        password = str(input("Password: ")).encode('utf-8')
        
        print('looking for user')
    
        for user in self.users or []:

            if str(user.get_username()) != username:
                continue
   
            print('user found, checking password')
            has = user.get_has()

            if verify(password).vl(has):
                print(f"{username} has logged in")
                break

            print('wrong password')
            break

        else:
            print('user doesn not have an account')



    def check_data(self):
        self.users = self.data.read()

class run:
    def __init__(self):
        pass

    def run(self):
        choice = str(input("sign-up or login: "))

        if choice == 'sign-up' or choice == 's':
            display().sign_up()

        elif choice == 'login' or choice == 'l':
            display().login()

        elif choice == 'wipe' or choice == 'w':
            with open('data.dat', 'wb') as file:
                pickle.dump([], file)
            
        else:
            print('error')

run().run()