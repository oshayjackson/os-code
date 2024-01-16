"""
& Author: Oshay M. Jackson
* Nasa open api project stage 1: Python gui
^ January 2024
"""


from user import User
import uuid


class Id:
    id_counter = 0

    def __init__(self):
        Id.id_counter += 1
        self.id = str(uuid.uuid4())[:3] + str(Id.id_counter)

    def generate_id(self):
        return self.id

    def echo_id(self):
        print(
            f"""
  AccountId
╭───────────╮
│    {self.id}   │
╰───────────╯
            """
        )


class Account:
    def __init__(self):
        self.uId = Id()
        self.userAccounts = []

    def add_user(self, user):
        user.user_id = self.uId.generate_id() + "_" + user.name
        self.userAccounts.append(user)
        return user.user_id

    def list_users(self):
        for user in self.userAccounts:
            print(
                f"""
User ID: {user.user_id}
Name: {user.name}
Password: {user.password}
                """
            )

    def pretty_data(self):
        for user in self.userAccounts:
            print(
                f"""
 ({user.name})
╭────────────────────────────────╮
    Account ID:   {self.uId.id}
    User ID:      {user.user_id}
    Name:         {user.name}
    Password:     {user.password}
╰────────────────────────────────╯
"""
            )


# Testing instances:

# test_account = Account()
# user_data1 = {"name": "oshay", "password": "password123"}
# user_data2 = {"name": "jackson", "password": "securepass"}
# user_id1 = test_account.add_user(user_data1)
# user_id2 = test_account.add_user(user_data2)
# test_account.pretty_data()
