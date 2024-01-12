#!/usr/bin/env python3


from email.mime import audio
from os import name


class User:
    def __init__(self):
        self.name = None
        self.auth = None
        self.account = None
        self.account_exists()  # & check account or not

    def account_exists(self):
        user = {'Name': None, 'Auth': None}
        account = input("Do you already have an account? (yes/no): ")

        if account.startswith('y'):
            print('Already have an account')
        elif account.startswith('n'):
            print('Let\'s create your account\n')
            self.name = user['Name'] = input("Enter name: ")
            self.auth = user['Auth'] = input("Enter a 5 digit password: ")
            self.account = user
            return self.account
        else:
            print('Invalid response')


# & Test instantiation
user_instance = User()

print("User Name:", user_instance.name)
print("User Auth:", user_instance.auth)
