wordbank = ["indentation", "spaces"]

tlgstudents = [
    "Albert",
    "Anthony",
    "Brenden",
    "Craig",
    "Deja",
    "Elihu",
    "Eric",
    "Giovanni",
    "James",
    "Joshua",
    "Maria",
    "Mohamed",
    "PJ",
    "Philip",
    "Sagan",
    "Suchit",
    "Meka",
    "Trey",
    "Winton",
    "Xiuxiang",
    "Yaping",
]

wordbank.append(str(4))


def fun():
    num = int(input("Enter a number between 0-20: "))

    # is valid range ?
    if 0 <= num < len(tlgstudents):
        student_name = tlgstudents[num]
        print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent")
    else:
        print("Invalid number. Please enter a number between 0 and 20.")


fun()
