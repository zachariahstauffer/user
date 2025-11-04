import Data
import User
import Verify
# import concurrent.futures
    
class Display:
    def __init__(self):
        self.users = []
        self.data = Data.Data()
        self.check_data()

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

        if Verify.Verify(password).verify_sign_up():
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

            if Verify.Verify(password).verify_login(has):
                print(f"{username} has logged in")
                break

            print('wrong password')
            break

        else:
            print('user doesn not have an account')

    def check_data(self):
        self.users = self.data.read()
   
if __name__ == '__main__':
    Display().run()