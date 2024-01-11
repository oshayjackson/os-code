#!/usr/bin/env python3


marvelchars = {
    "Starlord": {"real name": "peter quill", "powers": "dance moves", "archenemy": "Thanos"},
    "Mystique": {"real name": "raven darkholme", "powers": "shape shifter", "archenemy": "Professor X"},
    "Hulk": {"real name": "bruce banner", "powers": "super strength", "archenemy": "adrenaline"}
}


def get_user_input(prompt):
    return input(prompt).strip()


def capitalize_name(name):
    return ' '.join(part.capitalize() for part in name.split())


def start():
    while True:

        char_name = get_user_input(
            "Which character do you want to know about? (Starlord, Mystique, Hulk): ")
        char_stat = get_user_input(
            "What statistic do you want to know about? (real name, powers, archenemy): ")

        char_name = char_name.capitalize()

        if char_name in marvelchars and char_stat in marvelchars[char_name]:
            value = marvelchars[char_name][char_stat]
            if char_stat == "real name":
                value = capitalize_name(value)
            print(f"{char_name}'s {char_stat} is: {value}")
        else:
            print("Invalid input. Please enter a valid character name and statistic.")

        another = get_user_input("Do you want to try again? (yes/no): ")
        if another.lower() != 'yes' and another.startswith('y'):
            start()
        break


start()
