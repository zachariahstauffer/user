import tkinter as tk
from Data import Data
from Verify import Verify
from User import User

class Sign_up:
    def __init__(self):
        self.data = Data()
    
    def sign_up(self,  username, password):
        new_user = User(username, password)
        val, list_of_flags = Verify().verify_sign_up(username, password)

        if not val:
            return list_of_flags
        
        self.data.save(new_user)

class Login:
    def __init__(self):
        pass

    def login(self, username, password):

        exists, correct = Verify().verify_login(username, password)

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
        self.geometry("400x400")
        self.buttons()

    def buttons(self):
        self.login = tk.Button(self, text = 'login', command = self.login_button_click)
        self.signup = tk.Button(self, text = 'sign-up', command = self.sign_up_button_click)
        self.signup.grid(row=0, column=0, padx=20)
        self.login.grid(row=0, column=1, padx=20)

    def login_button_click(self):
        self.destroy_all()
        self.grid_columnconfigure(0, weight=1)

        self.textl1 = tk.Text(self, width= 30, height=1, wrap='none', font=('sans-serif', 10))
        self.textl2 = tk.Text(self, width= 30, height=1, wrap='none', font=('sans-serif', 10))
        submit = tk.Button(self, text="submit", command=self.login_helper)

        self.textl1.grid(row=0, column=0, pady=20)
        self.textl2.grid(row=1, column=0, pady=20)
        submit.grid(row=2, column=0)

    def sign_up_button_click(self):
        self.destroy_all()
        self.grid_columnconfigure(0, weight=1)

        self.texts1 = tk.Text(self, width= 30, height=1, wrap='none', font=('sans-serif', 10))
        self.texts2 = tk.Text(self, width= 30, height=1, wrap='none', font=('sans-serif', 10))
        submit = tk.Button(self, text="submit", command=self.sign_up_helper)

        self.texts1.grid(row=0, column=0, pady=20)
        self.texts2.grid(row=1, column=0, pady=20)
        submit.grid(row=3, column=0, pady=20)

    def login_helper(self):
        login = Login()

        login.login(self.textl1.get('1.0', 'end-1c'), self.textl2.get('1.0', 'end-1c'))

    def sign_up_helper(self):
        sign_up = Sign_up()

        flags = sign_up.sign_up(str(self.texts1.get('1.0', 'end-1c')), str(self.texts2.get('1.0', 'end-1c')))

        self.label_maker(flags)

    def label_maker(self, message = []):
        if message is []:
            return
        msg = ''
        for i in message:
            msg += f'{i} \n'

        label = tk.Label(self, text=msg, wraplength=300)

        label.grid_columnconfigure(0, weight=1)
        label.grid(row=2, column=0, pady=5)

    def destroy_all(self):
        for i in self.winfo_children():
            i.destroy()

app = App()
app.mainloop()