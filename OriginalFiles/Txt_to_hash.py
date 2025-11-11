import bcrypt

class Txt_to_hash:
    def __init__(self, text: str):
        self.text = text
        self.salt = bcrypt.gensalt()
        self.encode = text.encode('utf-8')
    
    def hashh(self):

        return bcrypt.hashpw(self.encode, self.salt)