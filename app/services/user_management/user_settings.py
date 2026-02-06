def change_password(self, VerifyClass, SignUpClass, SqliteClass, new_password):
    msg, val = VerifyClass().verify_password(new_password)

    if val:
        msg.append("password is strong")
        new_password = SignUpClass().password_to_hash(new_password)
        SqliteClass().change_password(self.id, new_password)

    return val, list

def delete_account(self, SqliteClass):
    SqliteClass().delete_user(self.id)
