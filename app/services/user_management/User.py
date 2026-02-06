from App.Services.Authentication.Verify import VerifyClass
from App.Services.DataBase.DataManager import SqliteClass
from App.Services.Authentication.SignUp import SignUpClass
from App.Services.UserManagement.UserSettings import *

class UserClass:
    def __init__(self, id, username: str, admin_status: bool):
        self.id = id
        self.username = username
        self.admin_status = admin_status

    def get_userID(self):
        return self.id
    
    def get_username(self):
        return self.username
    
    def get_admin(self):
        return self.admin_status

    def change_password(self, new_password):
        return change_password(self, VerifyClass, SignUpClass, SqliteClass, new_password)
    
    def delete_account(self):
        return delete_account(self, SqliteClass)
