from pymongo import MongoClient

class MoviesQueries:
    def __init__(self):
        db_name = 'pySamples'
        collection_name = 'movies'
        client = MongoClient('localhost', 27017)
        db = client[db_name]
        collection = db[collection_name]
        self.moviesCollection = collection

    # 1. Uzupełnij metodę zwracająca ilośc wszystkich filmów
    def count_movies(self):
        count = 0
        return count;
    # 2. Uzupełnij metodę zwracająca wszystkie filmy, w których wystąpiła Emma Watson
    def emma_watson_movies(self):
        ew_movies = None
        return ew_movies;

    # 3. Uzupełnij metodę zwracająca wszystkie filmy posiadające gatunek comedy oraz(and) fantasy
    def comedy_and_fantasy_movies(self):
        caf_movies = None
        return caf_movies