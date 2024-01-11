#!/usr/bin/env python3


def fav():
    user_list = []

    while True:
        name = input("\nWhat's your name?\nEnter here: ")
        age = int(input("\nHow old are you?\nEnter age: "))
        favorite_movie = input(
            "\nDo you have a favorite movie? (yes/no):\nEnter here: "
        ).lower()

        if favorite_movie.startswith("y"):
            movie = input("What's your favorite movie? Enter movie: ")
            genre = input("What genre is your favorite movie? Enter genre: ")
            actor = input("Who is your favorite actor in the movie? Enter actor: ")
        else:
            movie, genre, actor = None, None, None

        user_list.append(
            {
                "Name": name.capitalize(),
                "Age": age,
                "Favorite Movie": movie.capitalize() if movie else None,
                "Genre": genre.capitalize() if genre else None,
                "Favorite Actor": actor.capitalize() if actor else None,
            }
        )
        for x in user_list:
            print(x)

        return


fav()
