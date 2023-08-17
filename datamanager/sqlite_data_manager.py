from data_models import db, User, Movie, Review # imports the db and Movie classes from the data_models module
from datamanager.data_manager_interface import DataManagerInterface #managing interactions with an SQLite database


class SQLiteDataManager(DataManagerInterface): #implementing the methods
    def __init__(self, db_file_name): #constructor (initializer) for the SQLiteDataManager class
        self.db = db_file_name

    def list_all_users(self): #returns a list of all users in the database
        return User.query.all()
#retrieves the user with the given ID from the database and returns their list of favorite movies if the user exist
    def list_user_movies(self, user_id):
        user = User.query.get(user_id)
        if user:
            return user.favorite_movies
        return []

    def add_user(self, user): #adds a new user to the database
        self.db.session.add(user)
        self.db.session.commit()

    def add_movie(self, movie): #adds a new movie to the database
        self.db.session.add(movie)
        self.db.session.commit()

    def update_movie(self, movie): #updates an existing movie in the database
        existing_movie = Movie.query.get(movie.movie_id)
        if existing_movie:
            existing_movie.title = movie.title
            existing_movie.director = movie.director
            existing_movie.release_year = movie.release_year
            existing_movie.rating = movie.rating
            self.db.session.commit()

#method takes a movie_id as a parameter and delete a movie with that ID from the database
    def delete_movie(self, movie_id):
        movie = Movie.query.get(movie_id)
        if movie:
            self.db.session.delete(movie)
            self.db.session.commit()

    def commit(self): #commits any changes made to the database
        self.db.session.commit()

    def get_user_by_id(self, user_id): #retrieves a user from the database based on the provided user_id
        return User.query.get(user_id)

    def get_movie_by_id(self, movie_id): # retrieves a movie from the database based on the provided movie_id
        return Movie.query.get(movie_id)

    def list_all_reviews(self): #method retrieves a list of all reviews from the database
        reviews = Review.query.all()
        return reviews

    def get_review_by_id(self, review_id): # method retrieves a review from the database based on the provided review_id
        return Review.query.get(review_id)

    def delete_review(self, review): # method takes a review object as a parameter and deletes it from the database.
        db.session.delete(review)
        db.session.commit()
