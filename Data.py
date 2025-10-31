import pickle

class Data:
    def __init__(self,):
        self.users = []

    def save(self, users = []):
        with open('data.dat', 'wb') as file:
            pickle.dump(users, file)

    def read(self):
        try:

            file = open('data.dat', 'rb')
            self.users = pickle.load(file)

        except EOFError:
            self.users = []

        return self.users
    
    def wipe(self):
        with open('data.dat', 'wb') as file:
                pickle.dump([], file)
