from CoreFunctions.SignUp import Sign_up
from CoreFunctions.Login import Login
from CoreFunctions.Data import Data
from CoreFunctions.Verify import Verify
from CoreFunctions.AdminSettings import AdminSettings
from CoreFunctions.User import User


class CliApp:
    def __init__(self):
        self.sign_up = Sign_up()
        self.login = Login()
        self.data = Data()
        self.admin = AdminSettings()
        self.user = User

    def run(self):
        choice = str(input("[s]ign-up or [l]ogin: "))

        if choice == 'sign-up' or choice == 's':
            self.sign_up_prompt()

        elif choice == 'login' or choice == 'l':
            self.login_prompt()

        elif choice in ('admin', 'a'):
            self.admin_login()

        else:
            print('error')
   
    def sign_up_prompt(self):
        username = str(input('Make a username: '))
        password = str(input('Make a password: '))

        val, messages = self.sign_up.sign_up(username, password)

        if not val:
            self.message_handler(messages)
            self.sign_up_prompt()
            print()

            return

        self.message_handler(messages)

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

        messages, correct, self.user = self.login.login(username, password)

        self.message_handler(messages)

        if correct:
            self.user_settings(username)

    def admin_login(self):
        username = str(input('type in your admin username: ')).lower()
        password = str(input('type in your admin password: '))


        message, val = Verify().admin_login(username, password)
        print(message)

        if val:
            self.admin_prompts()
            return

    def user_settings(self, username):
        choice = str(input('[l]ogout, [d]elete: ')).lower()

        if choice in ('logout', 'l'):
            print(f'{username} has logged out')
            exit()
        elif choice in ('delete', 'd'):
            self.data.delete_user(username)
            print(f'{username} has been deleted')
            exit()

    '''
    def sign_up_helper(self, messages):
        pass

    def login_helper(self, messages):
        pass
    '''

    def message_handler(self, messages):
        print()
        message = ''
        for i in messages:
            message += f'{i}\n'
        print(message)

    def admin_prompts(self):
        print('''
              1. Delete a User
              2. Wipe All Data
              ''')


        choice = str(input("type the number: "))

        if choice == 1:
            user = input('username of the user to be deleted')
            
            self.admin.delete_user(user)

        elif choice == 2:
            self.admin.wipe_table()
 
if __name__ == '__main__':
    
    try:
        CliApp().run()
    except KeyboardInterrupt:
        print("\nprogram ends")