import tkinter as tk
from Data import Data
from Verify import Verify
from User import User

class Sign_up:
    def __init__(self):
        self.data = Data()
    
    def sign_up(self,  username, password):
        new_user = User(username, password)

        if not Verify(password).verify_sign_up():
            return
        print('signed up')
        self.data.save(new_user)

class Login:
    def __init__(self):
        pass

    def login(self, username, password):

        exists, correct = Verify(password).verify_login(username)

        if not exists:
            print(f'{username} does not have an account')
            return
        
        print(f'{username} was found')
        
        if correct:
            print(f'{username} has logged in')
            return
        else:
            print('wrong password')

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window()

    def window(self):
        self.title('quick app')
        self.config(bg='blue')
        self.geometry("200x200")
        self.buttons()

    def login_button_click(self):
        self.destroy_all()
        self.textl1 = tk.Text(self, width= 20, height=1)
        self.textl2 = tk.Text(self, width= 20, height=1)
        self.textl1.pack(anchor='center', pady=20)
        self.textl2.pack(anchor='s')
        submit = tk.Button(self, text="submit", command=self.login_helper)
        submit.pack(anchor='s', pady=20)

    def sign_up_button_click(self):
        self.destroy_all()
        self.texts1 = tk.Text(self, width= 20, height=1)
        self.texts2 = tk.Text(self, width= 20, height=1)
        self.texts1.pack(anchor='center', pady=20)
        self.texts2.pack(anchor='s')

        submit = tk.Button(self, text="submit", command=self.sign_up_helper)
        submit.pack(anchor='s', pady=20)

    def buttons(self):
        self.login = tk.Button(self, text = 'login', command = self.login_button_click)
        self.signup = tk.Button(self, text = 'sign-up', command = self.sign_up_button_click)
        self.login.pack(anchor='nw')
        self.signup.pack(anchor='nw')

    def login_helper(self):
        login = Login()

        login.login(self.textl1.get('1.0', 'end-1c'), self.textl2.get('1.0', 'end-1c'))

        self.destroy_all()
        self.buttons

    def sign_up_helper(self):
        sign_up = Sign_up()

        sign_up.sign_up(str(self.texts1.get('1.0', 'end-1c')), str(self.texts2.get('1.0', 'end-1c')))

        self.destroy_all()
        self.buttons()

    def destroy_all(self):
        for i in self.winfo_children():
            i.destroy()

app = App()
app.mainloop()