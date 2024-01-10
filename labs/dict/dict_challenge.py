#!/usr/bin/env python3

marvelchars = {
    "Starlord":
    {"real name": "peter quill",
     "powers": "dance moves",
     "archenemy": "Thanos"},

    "Mystique":
    {"real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"},

    "Hulk":
    {"real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"}
}


def kv():
    characters = '(Starlord, Mystique, Hulk)'
    statistics = '(real name, powers, archenemy)'
    i = 0
    for character in marvelchars:
        i += 1
    print(f'{i}) {character}\n')
    key_name = input(f'Enter the number: ')

    # key_value = input(f'What statistic do you want to know about? {
    #                   statistics}: ').lower()


characters = '(Starlord, Mystique, Hulk)'
statistics = '(real name, powers, archenemy)'

kv()
