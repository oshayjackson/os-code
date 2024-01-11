#!/usr/bin/env python3


def dracula():
    with open('./dracula.txt', 'r') as file:
        pylines = 0
        lineID = 0
        for line in file:
            pylines += 1
            lineID = pylines
            print(f'~ {lineID} - {line.strip()}')


if __name__ == '__main__':
    dracula()
