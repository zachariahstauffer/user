from .Data import DataClass

class AdminSettingsClass:
    def __init__(self):
        self.data = DataClass()

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