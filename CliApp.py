import Data
import User
import Verify
    
class CliApp:
    def __init__(self):
        self.data = Data.Data()

    def run(self):
        choice = str(input("[s]ign-up or [l]ogin: "))

        if choice == 'sign-up' or choice == 's':
            self.sign_up()

        elif choice == 'login' or choice == 'l':
            self.login()

        elif choice == 'wipe' or choice == 'w':
            Data.Data().wipe()
            
        else:
            print('error')

    def sign_up(self):
        print()

        username = str(input("Make Username: "))
        password = str(input("Make Password: "))

        new_user = User.User(username, password)

        val, list_of_flags = Verify.Verify().verify_sign_up(username, password)

        print()

        if not val:    
            for i in list_of_flags:
                print(f'{i}')

            print()

            self.sign_up()

            return
        
        print('signed up')

        self.data.save(new_user)
        
        print()

        choice = str(input(f'{username} has signed up, type [l]ogin, [b]ack, or [e]xit: '))

        if choice in ('login', 'l'):
            self.login()
            return
        elif choice in ('back', 'b'):
            self.run()
            return
        elif choice in ('exit','e'):
            exit()



    def login(self):
        print()

        username = str(input("Username: "))
        password = str(input("Password: "))

        exists, correct = Verify.Verify().verify_login(username, password)

        print()

        if not exists:
            print(f'{username} does not have an account')

            return
        
        print(f'{username} was found')
        
        if not correct:
            print('wrong password')
            self.login()
            return
        
        choice = str(input(f'{username} has logged in, type [s]ign-up, [b]ack, or [e]xit: '))

        if choice in ('sign-up', 's'):
            self.sign_up()

        elif choice in ('back','b'):
            self.run()

        elif choice in ('exit', 'e'):
            exit()

    def check_data(self, user):
        return self.data.load(user)
   
if __name__ == '__main__':
    CliApp().run()