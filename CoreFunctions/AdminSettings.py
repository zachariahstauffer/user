from CoreFunctions.Data import Data

class AdminSettings:
    def __init__(self):
        self.data = Data()

    def delete_user(self, username):
        self.data.delete_user(username)

    def wipe_table(self):
        self.data.wipe()

    def list_all_users(self):
        list = self.data.load_all_users()
        list2 = ''
        for i in list:
            list2 += f'{i}\n'

        return list2