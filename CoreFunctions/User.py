from .Verify import VerifyClass
from .Data import DataClass
from .SignUp import SignUpClass
import bcrypt



class UserClass:
    def __init__(self, id, username: str, is_admin: bool):
        self.id = id
        self.username = username
        self.is_admin = is_admin

    def get_user_id(self):
        return self.id
    
    def get_username(self):
        return self.username
    
    def change_password(self, new_password):
        val, list = VerifyClass().verify_password(new_password)
        message = ''

        for i in list:
            message += f'{i}'

        if val:
            new_password = SignUpClass().text_to_hash(new_password)
            DataClass().change_password(self.id, new_password)

        return message

    def delete_account(self):
        DataClass().delete_user(self.username)

    
    