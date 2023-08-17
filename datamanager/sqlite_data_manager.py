from datamanager.data_manager_interface import DataManagerInterface
from data_models import db,User, Movie, UserMovie, Review
from flask_sqlalchemy import SQLAlchemy



class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_file_name):
        self.db = db_file_name


    def list_all_users(self):
        return User.query.all()

    def list_user_movies(self, user_id):
        user = User.query.get(user_id)
        if user:
            return user.favorite_movies
        return []

    def add_user(self, user):
        self.db.session.add(user)
        self.db.session.commit()

    def add_movie(self, movie):
        self.db.session.add(movie)
        self.db.session.commit()

    def update_movie(self, movie):
        existing_movie = Movie.query.get(movie.movie_id)
        if existing_movie:
            existing_movie.title = movie.title
            existing_movie.director = movie.director
            existing_movie.release_year = movie.release_year
            existing_movie.rating = movie.rating
            self.db.session.commit()

    def delete_movie(self, movie_id):
        movie = Movie.query.get(movie_id)
        if movie:
            self.db.session.delete(movie)
            self.db.session.commit()

    def commit(self):
        self.db.session.commit()

    def get_user_by_id(self, user_id):
        return User.query.get(user_id)

    def get_movie_by_id(self, movie_id):
        return Movie.query.get(movie_id)

    def list_all_reviews(self):
        reviews = Review.query.all()
        return reviews

    def get_review_by_id(self, review_id):
        return Review.query.get(review_id)

    def delete_review(self, review):
        db.session.delete(review)
        db.session.commit()

