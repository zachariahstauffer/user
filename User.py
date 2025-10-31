import Txt_to_hash as tth

class User:
    def __init__(self, username: str, password):
        self.username = username
        self.has = b''
        self.hass(password)
    
    def get_username(self):
        return self.username
    
    def hass(self, password):
        self.has = tth.Txt_to_hash(password).hashh()

    def get_has(self):
        return self.has