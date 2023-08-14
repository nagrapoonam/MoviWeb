from MoviWeb.datamanager.data_manager_interface import DataManagerInterface
from MoviWeb.data_models import db, User, Movie, UserMovie
from flask_sqlalchemy import SQLAlchemy



class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_file_name):
        # self.db = SQLAlchemy(db_file_name)
        self.db = db_file_name
    # def __init__(self, app):
    #     self.db = SQLAlchemy(app)
    # def __init__(self, db):
    #     self.db = db
        # self.db = SQLAlchemy(db_file_name)
        # self.db = SQLAlchemy()
        # self.db.init_app(db_file_name)

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