#!/usr/bin/env python3

mylist = [1, 2, 3, 4, 5, "Python"]


def hello():
    # name= input(What is your name?\n>)
    name = input("What is your name?\n")

    return print(
        f"Hi {name.capitalize()}! Welcome to the Day {mylist[1]} of {mylist[5]}Python Training!"
    )


hello()
# This is what you should see when print runs-
# Hi <name>! Welcome to Day 2 of Python Training!
# print("Hi " + name.capitalize + "! Welcome to Day " + mylist[1] + " of " + mylist[6] " Training!")
