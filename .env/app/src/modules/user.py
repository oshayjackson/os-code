"""
& Author: Oshay M. Jackson
* Nasa open api project stage 1: Python gui
^ January 2024
"""


class User:
    def __init__(self, name=None, password=None):
        self.user_id = None  # Account class will init user_id
        self.name = name if name is not None else input("Enter name: ")
        self.password = password if password is not None else input("Enter password: ")
        self.data = {"Name": str(self.name), "password": self.password}

    def info(self):
        print(
            f"""
USER INFO
Name: {self.name}
User password: {self.password}

Thank you for signing up. Stay tuned for the upcoming
development of Nasa Astronomy Picture of the Day
"""
        )

    def export_user(self):
        return {"Name": self.name, "password": self.password}

    @classmethod
    def user_create(cls):
        return cls(None, None)
