import tkinter as tk
from CoreFunctions.SignUp import Sign_up
from CoreFunctions.Login import Login

class GuiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window()

    def window(self):
        self.title('quick app')
        self.config(bg='blue')
        self.geometry("400x400")
        self.start_window()

    def start_window(self):
        self.login = tk.Button(self, text = 'login', command = self.login_page)
        self.signup = tk.Button(self, text = 'sign-up', command = self.sign_up_page)
        self.signup.grid(row=0, column=0, padx=20)
        self.login.grid(row=0, column=1, padx=20)

    def login_page(self):
        self.destroy_all()
        self.grid_columnconfigure(0, weight=1)

        self.textl1 = tk.Text(self, width= 30, height=1, wrap='none', font=('sans-serif', 10))
        self.textl2 = tk.Text(self, width= 30, height=1, wrap='none', font=('sans-serif', 10))
        submit = tk.Button(self, text="submit", command=self.login_helper)

        self.textl1.grid(row=0, column=0, pady=20)
        self.textl2.grid(row=1, column=0, pady=20)
        submit.grid(row=2, column=0)

    def sign_up_page(self):
        self.destroy_all()
        self.grid_columnconfigure(0, weight=1)

        self.texts1 = tk.Text(self, width= 30, height=1, wrap='none', font=('sans-serif', 10))
        self.texts2 = tk.Text(self, width= 30, height=1, wrap='none', font=('sans-serif', 10))
        submit = tk.Button(self, text="submit", command=self.sign_up_helper)
        back = tk.Button(self, text='back', command=self.login_page)

        self.texts1.grid(row=0, column=0, pady=20)
        self.texts2.grid(row=1, column=0, pady=20)
        submit.grid(row=3, column=0, pady=20)
        back.grid(row=4, column=0, pady=20)

    def login_helper(self):
        login = Login()

        login.login(self.textl1.get('1.0', 'end-1c'), self.textl2.get('1.0', 'end-1c'))

    def sign_up_helper(self):
        sign_up = Sign_up()

        flags = sign_up.sign_up(str(self.texts1.get('1.0', 'end-1c')), str(self.texts2.get('1.0', 'end-1c')))

        self.label_maker(flags)

    def label_maker(self, message = []):
        
        msg = ''
        for i in message:
            msg += f'{i} \n'

        label = tk.Label(self, text=msg, wraplength=300)

        label.grid_columnconfigure(0, weight=1)
        label.grid(row=2, column=0, pady=5)

    def back(self):
        self.destroy_all()
        self.start_window

    def destroy_all(self):
        for i in self.winfo_children():
            i.destroy()

if __name__ == '__main__':
    app = GuiApp()
    app.mainloop()