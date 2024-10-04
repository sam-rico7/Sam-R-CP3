class Movie:
    def __init__(self, name, year, director, rating, genre, cast):
        self.name = name
        self.year = year
        self.director = director
        self.rating = rating
        self.genre = genre
        self.cast = cast

    def __str__(self):
        return f"Name: {self.name}\nYear: {self.year}\nDirector: {self.director}\nRating: {self.rating}\nGenre: {self.genre}\nCast: {', '.join(self.cast)}"

def sort_movies_alphabetically(movies):
    sorted_movies = []
    while movies:
        min_movie = movies[0]
        for movie in movies:
            if movie.name < min_movie.name:
                min_movie = movie
        sorted_movies.append(min_movie)
        movies.remove(min_movie)
    return sorted_movies

def sort_movies_chronologically(movies):
    sorted_movies = []
    while movies:
        min_movie = movies[0]
        for movie in movies:
            if movie.year < min_movie.year:
                min_movie = movie
        sorted_movies.append(min_movie)
        movies.remove(min_movie)
    return sorted_movies

def search_by_genre(movies, genre):
    found_movies = []
    for movie in movies:
        if movie.genre.lower() == genre.lower():
            found_movies.append(movie)
    return found_movies

def search_by_director(movies, director):
    found_movies = []
    for movie in movies:
        if movie.director.lower() == director.lower():
            found_movies.append(movie)
    return found_movies

def search_by_cast(movies, actor):
    found_movies = []
    for movie in movies:
        if actor.lower() in [member.lower() for member in movie.cast]:
            found_movies.append(movie)
    return found_movies

def display_menu():
    print("\n=== Movie Management Menu ===")
    print("1. View Movies Sorted Alphabetically")
    print("2. View Movies Sorted Chronologically")
    print("3. Search Movies by Genre")
    print("4. Search Movies by Director")
    print("5. Search Movies by Cast Member")
    print("6. Exit")
    print("==============================")

movies = [
    Movie("The Shawshank Redemption", 1994, "Frank Darabont", "R", "Drama", ["Tim Robbins", "Morgan Freeman"]),
    Movie("Pulp Fiction", 1994, "Quentin Tarantino", "R", "Crime", ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]),
    Movie("The Godfather", 1972, "Francis Ford Coppola", "R", "Crime", ["Marlon Brando", "Al Pacino", "James Caan"]),
    Movie("Inception", 2010, "Christopher Nolan", "PG-13", "Sci-Fi", ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]),
    Movie("The Matrix", 1999, "Lana Wachowski, Lilly Wachowski", "R", "Sci-Fi", ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]),
    Movie("Forrest Gump", 1994, "Robert Zemeckis", "PG-13", "Drama", ["Tom Hanks", "Robin Wright", "Gary Sinise"]),
    Movie("The Dark Knight", 2008, "Christopher Nolan", "PG-13", "Action", ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]),
    Movie("Schindler's List", 1993, "Steven Spielberg", "R", "Drama", ["Liam Neeson", "Ben Kingsley", "Ralph Fiennes"]),
    Movie("Fight Club", 1999, "David Fincher", "R", "Drama", ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"]),
    Movie("Goodfellas", 1990, "Martin Scorsese", "R", "Crime", ["Robert De Niro", "Ray Liotta", "Joe Pesci"]),
    Movie("The Silence of the Lambs", 1991, "Jonathan Demme", "R", "Thriller", ["Jodie Foster", "Anthony Hopkins", "Scott Glenn"]),
    Movie("Titanic", 1997, "James Cameron", "PG-13", "Romance", ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane"]),
    Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Peter Jackson", "PG-13", "Fantasy", ["Elijah Wood", "Ian McKellen", "Orlando Bloom"]),
    Movie("Gladiator", 2000, "Ridley Scott", "R", "Action", ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"]),
    Movie("The Green Mile", 1999, "Frank Darabont", "R", "Drama", ["Tom Hanks", "Michael Clarke Duncan", "David Morse"]),
    Movie("Saving Private Ryan", 1998, "Steven Spielberg", "R", "War", ["Tom Hanks", "Matt Damon", "Tom Sizemore"]),
    Movie("Jurassic Park", 1993, "Steven Spielberg", "PG-13", "Adventure", ["Sam Neill", "Laura Dern", "Jeff Goldblum"]),
    Movie("The Departed", 2006, "Martin Scorsese", "R", "Crime", ["Leonardo DiCaprio", "Matt Damon", "Jack Nicholson"]),
    Movie("The Lion King", 1994, "Roger Allers, Rob Minkoff", "G", "Animation", ["Matthew Broderick", "Jeremy Irons", "James Earl Jones"]),
    Movie("Eternal Sunshine of the Spotless Mind", 2004, "Michel Gondry", "R", "Romance", ["Jim Carrey", "Kate Winslet", "Kirsten Dunst"]),
    Movie("The Sixth Sense", 1999, "M. Night Shyamalan", "PG-13", "Thriller", ["Bruce Willis", "Haley Joel Osment", "Toni Collette"]),
    Movie("The Usual Suspects", 1995, "Bryan Singer", "R", "Mystery", ["Kevin Spacey", "Gabriel Byrne", "Chazz Palminteri"]),
    Movie("Memento", 2000, "Christopher Nolan", "R", "Thriller", ["Guy Pearce", "Carrie-Anne Moss", "Joe Pantoliano"]),
    Movie("Braveheart", 1995, "Mel Gibson", "R", "Biography", ["Mel Gibson", "Sophie Marceau", "Patrick McGoohan"]),
    Movie("The Terminator", 1984, "James Cameron", "R", "Sci-Fi", ["Arnold Schwarzenegger", "Linda Hamilton", "Michael Biehn"]),
    Movie("Back to the Future", 1985, "Robert Zemeckis", "PG", "Adventure", ["Michael J. Fox", "Christopher Lloyd", "Lea Thompson"]),
    Movie("Alien", 1979, "Ridley Scott", "R", "Horror", ["Sigourney Weaver", "Tom Skerritt", "John Hurt"]),
    Movie("The Truman Show", 1998, "Peter Weir", "PG", "Drama", ["Jim Carrey", "Laura Linney", "Noah Emmerich"]),
    Movie("The Breakfast Club", 1985, "John Hughes", "R", "Comedy", ["Molly Ringwald", "Emilio Estevez", "Judd Nelson"]),
    Movie("Dead Poets Society", 1989, "Peter Weir", "PG", "Drama", ["Robin Williams", "Robert Sean Leonard", "Ethan Hawke"]),
    Movie("Ferris Bueller's Day Off", 1986, "John Hughes", "PG-13", "Comedy", ["Matthew Broderick", "Alan Ruck", "Mia Sara"]),
    Movie("The Perks of Being a Wallflower", 2012, "Stephen Chbosky", "PG-13", "Drama", ["Logan Lerman", "Emma Watson", "Ezra Miller"]),
    Movie("Dazed and Confused", 1993, "Richard Linklater", "R", "Comedy", ["Jason London", "Wiley Wiggins", "Matthew McConaughey"])
]

while True:
    display_menu()
    choice = input("Please select an option (1-6): ")

    if choice == '1':
        print("\nMovies sorted alphabetically:")
        sorted_movies = sort_movies_alphabetically(movies.copy())
        for movie in sorted_movies:
            print(movie)
    elif choice == '2':
        print("\nMovies sorted chronologically:")
        sorted_movies = sort_movies_chronologically(movies.copy())
        for movie in sorted_movies:
            print(movie)
    elif choice == '3':
        genre = input("Enter the genre to search for: ")
        print(f"\nMovies in the '{genre}' genre:")
        found_movies = search_by_genre(movies, genre)
        for movie in found_movies:
            print(movie)
    elif choice == '4':
        director = input("Enter the director's name to search for: ")
        print(f"\nMovies directed by '{director}':")
        found_movies = search_by_director(movies, director)
        for movie in found_movies:
            print(movie)
    elif choice == '5':
        actor = input("Enter the actor's name to search for: ")
        print(f"\nMovies with '{actor}' in the cast:")
        found_movies = search_by_cast(movies, actor)
        for movie in found_movies:
            print(movie)
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")