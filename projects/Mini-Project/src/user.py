
class User:
    def __init__(self, name=None, pin=None):
        self.name = name if name is not None else input('Enter name: ')
        self.pin = pin if pin is not None else input('Enter 4 digit pin: ')
        self.data = {'Name': str(self.name), 'Pin': int(self.pin)}

    def info(self):
        print(f"""
USER INFO
Name: {self.name}
User Pin: {self.pin}
"""
        )

    def export_user(self):
        return {"Name": self.name, "Pin": self.pin}

    @classmethod
    def user_create(cls):
        return cls(None, None)


# if __name__ == "__main__":
#     pass
# usr1 = User('oshay', 1234)
# usr1.info()
# the above code allows for optional params
