import bcrypt

class User:
    def __init__(self, username: str, id):
        self.username = username
        self.id = id

    def get_user_id(self):
        return self.id
    
    def get_username(self):
        return self.username
    
    