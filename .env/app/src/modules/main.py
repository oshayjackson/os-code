#!/usr/bin/env python3

"""
& Author: Oshay M. Jackson
* Nasa open api project stage 1: Python gui
^ January 2024
"""


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from user import User
from account import Account

ASSETS = Path(r"./assets/")


def relative_to_assets(path: str) -> Path:
    return ASSETS / Path(path)


def main():
    window = Tk()
    window.title("Nasa Api")
    window.geometry("600x800")
    window.configure(bg="#2F3A4D")
    # <br>

    userAccount = Account()

    def on_button_click():
        global user  # for the user that is or was created
        name = entry_1.get()
        password = entry_2.get()
        user = User(name, password)
        user_id = userAccount.add_user(user)
        user.info()
        print(
            "Do you want to view your account data? (Click Account data button or (Ctrl+c) to quit: "
        )

        # ^--Clear Text
        entry_1.delete(0, "end")
        entry_2.delete(0, "end")

    def show_account_data():
        userAccount.pretty_data()

    canvas = Canvas(
        window,
        bg="#2F3A4D",
        height=800,
        width=600,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    canvas.place(x=0, y=0)
    # <br>

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(306.0, 424.0, image=entry_image_1)
    entry_1 = Entry(
        bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0
    )  #!****** entry name
    entry_1.place(x=86.0, y=399.0, width=440.0, height=48.0)
    # <br>
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(306.0, 318.0, image=entry_image_2)
    entry_2 = Entry(
        bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0
    )  #!****** entry password
    entry_2.place(x=86.0, y=293.0, width=440.0, height=48.0)
    # <br>
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(72.0, 749.0, image=image_image_1)
    # <br>
    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(148.0, 749.0, image=image_image_2)
    # <br>
    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(224.0, 749.0, image=image_image_3)
    # <br>
    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(300.0, 749.0, image=image_image_4)
    # <br>
    image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(380.0, 749.0, image=image_image_5)
    # <br>
    image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(300.0, 104.0, image=image_image_6)
    # <br>
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    # <br>
    canvas.create_text(
        77.0,
        273.0,
        anchor="nw",
        text="Enter your name:",
        fill="#FFFFFF",
        font=("Inter SemiBold", 12 * -1),
    )

    # <br>
    canvas.create_text(
        77.0,
        379.0,
        anchor="nw",
        text="Create a password:",
        fill="#FFFFFF",
        font=("Inter SemiBold", 12 * -1),
    )
    # <br>

    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=on_button_click,
        relief="flat",
    )

    button_1.place(x=244.0, y=500.0, width=112.0, height=37.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=show_account_data,
        relief="flat",
    )
    button_2.place(x=438.0, y=731.0, width=112.0, height=37.0)

    window.mainloop()


if __name__ == "__main__":
    main()
