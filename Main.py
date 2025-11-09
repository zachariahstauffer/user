import Data
import User
import Verify
# import concurrent.futures
    
class Display:
    def __init__(self):
        self.data = Data.Data()

    def run(self):
        choice = str(input("sign-up or login: "))

        if choice == 'sign-up' or choice == 's':
            self.sign_up()

        elif choice == 'login' or choice == 'l':
            self.login()

        elif choice == 'wipe' or choice == 'w':
            Data.Data().wipe()
            
        else:
            print('error')

    def sign_up(self):
        username = str(input("Make Username: "))
        password = str(input("Make Password: "))

        new_user = User.User(username, password)
        
        self.data.save(new_user)

    def login(self):
        username = str(input("Username: "))
        password = str(input("Password: ")).encode('utf-8')
        hashed_password = self.check_data(username)

        if Verify.Verify(password).verify_login(hashed_password):
            print('logged in')
            return
        
        print('wrong password')
        

    
    def check_data(self, user):
        return self.data.load(user)
   
if __name__ == '__main__':
    Display().run()