from .Verify import VerifyClass
from .DataManager import SqliteClass
from .SignUp import SignUpClass

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
        val, list = VerifyClass().verify_password(new_password)

        if val:
            list.append("password is strong")
            new_password = SignUpClass().text_to_hash(new_password)
            SqliteClass().change_password(self.id, new_password)

        return val, list

    def delete_account(self):
        SqliteClass().delete_user(self.id)

