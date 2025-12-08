from .Verify import VerifyClass
from .Data import DataClass
from .SignUp import SignUpClass
import bcrypt

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
            DataClass().change_password(self.id, new_password)

        return val, list

    def delete_account(self):
        DataClass().delete_user(self.id)

