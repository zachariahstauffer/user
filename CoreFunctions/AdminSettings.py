from CoreFunctions.Data import Data

class AdminSettings:
    def __init__(self):
        self.data = Data()

    def delete_user(self, username):
        self.data.delete_user(username)

    def wipe_table(self):
        self.data.wipe()