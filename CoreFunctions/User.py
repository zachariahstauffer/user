
class User:
    def __init__(self, id, username: str, is_admin: bool):
        self.id = id
        self.username = username
        self.is_admin = is_admin

    def get_user_id(self):
        return self.id
    
    def get_username(self):
        return self.username
    
    def change_password(self):
        pass

    def delete_account(self):
        pass
    
    