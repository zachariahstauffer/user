import bcrypt
import pickle

class data:
    def __init__(self,):
        self.users = []

    def save(self, users = []):
        with open('data.dat', 'wb') as file:
            pickle.dump(users, file)

    def read(self):
        try:

            with open('data.dat', 'rb') as file:
                self.users = pickle.load(file)

        except EOFError:
            self.users = []

        return self.users

class txt_to_hash:
    def __init__(self, tx: str):
        self.tx = tx
        self.s = bcrypt.gensalt()
        self.en = tx.encode('utf-8')
        self.has = self.hashh()
    
    def hashh(self):

        return bcrypt.hashpw(self.en, self.s)

class user:
    def __init__(self, username: str, password):
        self.username = username
        self.password = password
        self.has = b''
        self.hass()
    
    def get_username(self):
        return self.username
    
    def hass(self):
        self.has = txt_to_hash(self.password)

    def get_has(self):
        return self.has
    
class verify:
    def __init__(self, password, has):
        self.password = password
        self.has = has.has

    def vf(self):

        return bool(bcrypt.checkpw(self.password, self.has))
    
class display:
    def __init__(self):
        self.users = []
        self.data = data()
        self.check_data()

    def sign_up(self):
        username = str(input("Make Username: "))
        password = str(input("Make Password: "))

        new_user = user(username, password)

        self.users.append(new_user)

        self.data.save(self.users)

    def login(self):
        username = str(input("Username: "))
        password = str(input("Password: ")).encode('utf-8')
    
        for user in self.users or []:

            print('looking for user')

            if str(user.get_username()) == username:
   
                print('user found, checking password')
                has = user.get_has()

                if verify(password, has):
                    print(f"{username} has logged in")
                break

    def check_data(self):
        self.users = self.data.read()

class run:
    def __init__(self):
        pass

    def run(self):
        choice = str(input("type su for sign up or lg for login: "))

        if choice == 'su':
            display().sign_up()

        elif choice == 'lg':
            display().login()

        elif choice == 'wipe':
            with open('data.dat', 'wb') as file:
                pickle.dump({}, file)
            
        else:
            print('error')

run().run()