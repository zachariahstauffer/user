import Txt_to_hash as tth

class User:
    def __init__(self, username: str, password):
        self.username = username
        self.hash_val = b''
        self.hashed(password)
    
    def get_username(self):
        return self.username
    
    def hashed(self, password):
        self.hash_val = tth.Txt_to_hash(password).hashh()

    def get_hash(self):
        return self.hash_val