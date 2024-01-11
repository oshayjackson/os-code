#!/usr/bin/env python3

heroes = ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]

# PART 1
# Print out your favorite character from this list!
mine = heroes[3]


def myhero():
    print(f"My favorite hero is {mine}!")


myhero()


# PART 2
# Ask the user to pick a number between 1 and 100.
def pick():
    num = int(input("Pick a number between 1 and 100\nEnter number here: "))


pick()

# PART 3
# check out https://docs.python.org/3/library/functions.html or go to Google
# use a built-in function to find which integer in nums is the biggest.
# then, print out that number!

nums = [1, -5, 56, 987, 0]
x = max(nums)
print(x)
