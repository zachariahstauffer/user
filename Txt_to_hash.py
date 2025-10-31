import bcrypt

class Txt_to_hash:
    def __init__(self, tx: str):
        self.tx = tx
        self.s = bcrypt.gensalt()
        self.en = tx.encode('utf-8')
    
    def hashh(self):

        return bcrypt.hashpw(self.en, self.s)