challenge = ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial = ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare = [{"slappy": "a", "text": "b", "kumquat": "goggles", "user": {
    "awesome": "c", "name": {"first": "eyes", "last": "toes"}}, "banana": 15, "d": "nothing"}]


def slice():
    print('\n')
    print('Challenge:')
    print(f'My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}\n')

    print('Trial:')
    print(f'My {trial[2]["eyes"]}! The {trial[2]["goggles"]} do {trial[3]}\n')

    print('Nightmare:')
    print(f'My {nightmare[0]["user"]["name"]["first"]}! The {
          nightmare[0]["kumquat"]} do {nightmare[0]["d"]}\n')


slice()
