
from account_id import Id
from user import User


class Account:
    def __init__(self):
        self.account_id = Id()
        self.users = {}

    def add(self, user):
        # Initialize a unique user ID for each user within the account
        user.user_id = self.account_id.id + "_" + user.name
        self.users[user.user_id] = user
        print(f"User {user.name} with User ID {
              user.user_id} is now associated with Account {self.account_id.id}")
        return user.user_id

    def get(self, user_id):
        return self.users.get(user_id)

    def list(self):
        print(f"Users in Account {self.account_id.id}:")
        for user_id, user in self.users.items():
            print(f"User ID: {user_id}, Name: {user.name}, Pin: {user.pin}")

    def export_account(self):
        account_data = {
            "AccountID": self.account_id.id,
            "Users": {user_id: user.export_user() for user_id, user in self.users.items()}
        }
        return account_data


# if __name__ == "__main__":
#     print('')
#     account1 = Account()
#     user1 = User(name="Alice", pin="1234")

#     user_id1 = account1.add_user(user1)
#     account1.list_users()

#     # Export account data with user IDs
#     account_data = account1.export_account()
#     print("Account Data:", account_data)
#     print('')
