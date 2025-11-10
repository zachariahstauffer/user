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

        if not Verify.Verify(password).verify_sign_up():
            return
        print('signed up')
        self.data.save(new_user)

    def login(self):
        username = str(input("Username: "))
        password = str(input("Password: ")).encode('utf-8')

        exists, correct = Verify.Verify(password).verify_login(username)

        if not exists:
            print(f'{username} does not have an account')
            return
        
        print(f'{username} was found')
        
        if correct:
            print(f'{username} has logged in')
            return
        else:
            print('wrong password')

            

    def check_data(self, user):
        return self.data.load(user)
   
if __name__ == '__main__':
    Display().run()