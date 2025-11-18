from CoreFunctions.SignUp import Sign_up
from CoreFunctions.Login import Login
from CoreFunctions.Data import Data
    
class CliApp:
    def __init__(self):
        self.sign_up = Sign_up()
        self.login = Login()
        self.data = Data()

    def run(self):
        choice = str(input("[s]ign-up or [l]ogin: "))

        if choice == 'sign-up' or choice == 's':
            self.sign_up_prompt()

        elif choice == 'login' or choice == 'l':
            self.login_prompt()

        elif choice == 'wipe' or choice == 'w':
            self.data.wipe()
            
        else:
            print('error')
   
    def sign_up_prompt(self):
        username = str(input('Make a username: '))
        password = str(input('Make a password: '))

        val, messages = self.sign_up.sign_up(username, password)

        if not val:
            self.sign_up_helper(messages)
            self.sign_up_prompt()
            print()

            return

        self.login_helper(messages)

        choice = str(input(f'{username} has signed up, type [l]ogin, [b]ack, or [e]xit: ')).lower()

        if choice in ('login', 'l'):
            print()
            self.login_prompt()
            return
        elif choice in ('back', 'b'):
            print()
            self.run()
            return
        elif choice in ('exit', 'e'):
            exit()

    def login_prompt(self):
        username = str(input('Type your username: '))
        password = str(input('Type your password: '))

        messages, correct = self.login.login(username, password)

        self.login_helper(messages)

        if correct:
            self.user_settings(username)

    def user_settings(self, username):
        choice = str(input('[l]ogout, [d]elete: ')).lower()

        if choice in ('logout', 'l'):
            print(f'{username} has logged out')
            exit()
        elif choice in ('delete', 'd'):
            self.data.delete_user(username)
            print(f'{username} has been deleted')
            exit()

    def sign_up_helper(self, messages):
        print()
        message = ''
        for i in messages:
            message += f'{i}\n'

        print(message)

    def login_helper(self, messages):
        print()
        message = ''
        for i in messages:
            message += f'{i}\n'
        print(message)
    
    '''
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
    '''
    def check_data(self, user):
        return self.data.load(user)
   
if __name__ == '__main__':
    
    try:
        CliApp().run()
    except KeyboardInterrupt:
        print("\nprogram ends")