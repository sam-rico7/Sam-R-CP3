

class Movie:
    def __init__(self, name, year, director, cast, rating, genre):
        self.name = name
        self.year = year
        self.director = director
        self.cast = cast
        self.rating = rating
        self.genre = genre
    
    def __str__(self):
        return f"Name: {self.name}\nYear: {self.year}\nDirector: {self.director}\nCast: {self.cast}\nRating: {self.rating}"
    


movie1 = Movie("The Shawshank Redemption", 1994, "Frank Darabont", "Tim Robbins, Morgan Freeman", "R", "Drama" )
movie2 = Movie("Pulp Fiction", 1994, "Quentin Tarantino", "John Travolta, Uma Thurman, Samuel L. Jackson", "R", "Crime")
movie3 = Movie("The Godfather", 1972, "Francis Ford Coppola", "Marlon Brando, Al Pacino, James Caan", "R", "Crime")
movie4 = Movie("Inception", 2010, "Christopher Nolan", "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page", "PG-13", "Sci-Fi")
movie5 = Movie("The Matrix", 1999, "Lana Wachowski, Lilly Wachowski", "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss", "R", "Sci-Fi")
movie6 = Movie("Forrest Gump", 1994, "Robert Zemeckis", "Tom Hanks, Robin Wright, Gary Sinise", "PG-13", "Drama")
movie7 = Movie("The Dark Knight", 2008, "Chrisopher Nolan", "Christian Bale, Heath Ledger, Aaron Eckhart", "PG-13", "Action")
movie8 = Movie("Schindler's List", 1993, "Steven Spielberg", "Liam Neeson, Ben Kingsley, Ralph Fiennes", "R", "Drama")
movie9 = Movie("Fight Club", 1999,"David Fincher", "Brad Pitt, Edward Norton, Helena Bonham Carter", "R", "Drama")

def sort_movie():
    

