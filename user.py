from storage import Storage

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    @staticmethod
    def add_user(name, user_id):
        new_user = {
            'name': name,
            'user_id': user_id
        }
        users = Storage.load_data('users.json')
        users.append(new_user)
        Storage.save_data('users.json', users)

    @staticmethod
    def update_user(user_id, updated_data):
        users = Storage.load_data('users.json')
        for user in users:
            if user['user_id'] == user_id:
                user.update(updated_data)
                break
        Storage.save_data('users.json', users)

    @staticmethod
    def delete_user(user_id):
        users = Storage.load_data('users.json')
        users = [user for user in users if user['user_id'] != user_id]
        Storage.save_data('users.json', users)

    @staticmethod
    def list_users():
        users = Storage.load_data('users.json')
        for user in users:
            print(f"Name: {user['name']}, User ID: {user['user_id']}")

    @staticmethod
    def search_user(**kwargs):
        users = Storage.load_data('users.json')
        found_users = []
        for user in users:
            if all(user[k] == v for k, v in kwargs.items()):
                found_users.append(user)
        return found_users
