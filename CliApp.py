from getpass import getpass
from CoreFunctions import SignUpClass, LoginClass, AdminSettingsClass

# Are you still using this? We could probably delete it soon

class CliApp:
    def __init__(self):
        self.sign_up = SignUpClass()
        self.login = LoginClass()
        self.admin = AdminSettingsClass()
        self.user = None

    def run(self):
        choice = str(input("[s]ign-up or [l]ogin: "))

        if choice == 'sign-up' or choice == 's':
            self.sign_up_prompt()

        elif choice == 'login' or choice == 'l':
            self.login_prompt()

        else:
            print('error')

    def sign_up_prompt(self):
        username = str(input('Make a username: '))
        password = str(getpass('Make a password: '))

        messages, passed = self.sign_up.sign_up(username, password)

        if not passed:
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

        messages, correct_password, self.user = self.login.login(username, password)

        if not correct_password:
            self.message_handler(messages)

        self.message_handler(messages)
        self.admin_check()

    def user_settings_prompts(self):
        if self.user is None:
            return

        print('''
              1. change password
              2. delete account
              3. logout
              ''')

        choice = input('Type the number: ')

        if choice == '1':
            new_password = input('new password')
            self.user.change_password(new_password)
        elif choice == '2':
            self.user.delete_account()
        elif choice == '3':
            exit()
        else:
            print('error')

    def admin_settings_prompts(self):
        print('''
              1. delete a user
              2. wipe all data
              3. list all users
              ''')
        
        choice = input('type a number: ')

        if choice == '1':
            pass
        elif choice == '2':
            self.admin.wipe_table()
        elif choice == '3':
            list = self.admin.list_all_users()
            print(list)
        else:
            print('toast')

    def admin_check(self):
        if self.user is None:
            print('No User Loaded')
            return

        if self.user.get_user_id() == 0:
            self.admin_settings_prompts()
        else:
            self.user_settings_prompts()

    def message_handler(self, messages):
        print()
        message = ''
        for i in messages:
            message += f'{i}\n'
        print(message + '\n')

if __name__ == '__main__':
    
    try:
        CliApp().run()
    except KeyboardInterrupt:
        print("\nprogram ends")
