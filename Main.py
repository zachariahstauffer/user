import Data
import User
import Verify
# import concurrent.futures
    
class Display:
    def __init__(self):
        self.users = []
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
        
        self.data.save(self.users)

    def login(self):
        username = str(input("Username: "))
        password = str(input("Password: ")).encode('utf-8')
        
        print('looking for user')

        
    
        def check_data(self, user):
            pass
   
if __name__ == '__main__':
    Display().run()