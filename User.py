import bcrypt

class User:
    def __init__(self, username: str, password):
        self.username = username
        self.hash_val = b''
        self.hashed(password)
    
    def get_username(self):
        return self.username
    
    def hashed(self, password):
        self.hash_val = self.text_to_hash(password)

    def get_hash(self):
        return self.hash_val
    
    def text_to_hash(self, password):
        password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password, salt)