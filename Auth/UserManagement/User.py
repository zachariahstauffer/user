from ..Verifacation.Verify import VerifyClass
from ..DataManager import SqliteClass
from ..Authentication.SignUp import SignUpClass
from ..Admin.UserSettings import change_password, delete_account

class UserClass:
    def __init__(self, id, username: str, admin_status: bool):
        self.id = id
        self.username = username
        self.admin_status = admin_status

    def get_user_id(self):
        return self.id
    
    def get_username(self):
        return self.username
    
    def get_admin(self):
        return self.admin_status

    def change_password(self, new_password):
        return change_password(self, VerifyClass, SignUpClass, SqliteClass, new_password)
    
    def delete_account(self):
        return delete_account(self, SqliteClass)
