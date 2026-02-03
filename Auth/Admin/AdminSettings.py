from ..DataManager import SqliteClass

class AdminSettingsClass:
    def __init__(self):
        self.data = SqliteClass()

    def promote_user_demote_admin(self, username):
        id, admin, _ = self.data.load(username)

        if not admin:
            self.data.change_admin_status(id, True)
        elif admin:
            self.data.change_admin_status(id, False)

    def delete_user(self, username):
        id, _, _ = self.data.load(username)

        self.data.delete_user(id)

    def wipe_table(self):
        self.data.wipe()

    def list_all_users(self):
        users = self.data.load_all_users()

        if not users:
            return 'No users found'
        
        output = f"Total Users: {len(users)}\n\n"

        for user in users:
            id, admin, username, _ = user

            status = "ADMIN" if admin else "user"

            output += f"ID: {id} | {status} | {username}\n"

        return output

    def stats(self):
        users = self.data.load_all_users()

        if not users:
            return "No users found"
        
        total_users = len(users)
        admin_count = 0
        user_count = 0
        
        for user in users:
            _, admin, _, _ = user

            if admin:
                admin_count += 1
            else:
                user_count += 1

        return total_users, admin_count, user_count
