movies = {
    "action":{
        "Avengers": 5,
        "Batman": 4,
        "Spiderman": 3
    },
    "comedy":{
        "The Hangover": 4,
        "Superbad": 5,
        "Step Brothers": 3
    },
    "drama":{
        "The Shawshank Redemption": 5,
        "The Godfather": 4,
        "Forrest Gump": 3
    },
    "horror":{
        "The Conjuring": 4,
        "It": 5,
        "A Quiet Place": 3
    },
    "series":{
        "Breaking Bad": 5,
        "Game of Thrones": 4,
        "Stranger Things": 3
    },
    "si-fi":{
        "Inception": 5,
        "Interstellar": 4,
        "The Matrix": 3
    }
}

print("Welcome to the Movie Recommendation System!")

while True:
    print("\n Availabe genres: ")
    for genre in movies:
        print(f"- {genre}")
    
    choice = input("\n Enter a genre to get movie recommendations (or 'exit' to quit): ").lower()
    if choice == 'exit':
        print("Thank you for using the Movie Recommendation System. Goodbye!")
        break
    elif choice in movies:
        print(f"\n Recommended movies in {choice} genre:")
        for movie, rating in movies[choice].items():
            print(f"{movie} (Rating: {rating}/5)")
    else:
        print("Invalid genre. Please try again.")

    liked_movies = input("\n Enter movies you liked from the list above: ")
    if liked_movies in movies[choice]:
        print(f"\n Based on your liking of {liked_movies}, you might also like:")
        for movie, rating in movies[choice].items():
            if movie != liked_movies and rating >=4:
                print(f"{movie} (Rating: {rating}/5)")