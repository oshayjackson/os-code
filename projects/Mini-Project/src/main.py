#!/usr/bin/env python3


from user import User
from account import Account


def main():
    # create instance of Account()
    user_account = Account()
    def create_user(): return user_account.add(User.user_create())
    create_user()

    # display user information
    user_account.list()

    # Export account data
    account_data = user_account.export_account()
    print("Account Overview:", account_data)


if __name__ == "__main__":
    main()
