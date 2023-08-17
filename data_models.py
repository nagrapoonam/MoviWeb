from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """ Define the User class as a subclass of Base (declarative_base).
    Defines columns for the user table: id, username, email, and password."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # primary key, autoincrement
    username = db.Column(db.String(100), nullable=False)  # stores the user's username
    email = db.Column(db.String(100), nullable=False, unique=True)  # stores the user's email
    password = db.Column(db.String(100), nullable=False)  # stores the user's password

    # Define the relationship with favorite_movies
    favorite_movies = db.relationship("Movie", secondary="user_movie",
                                      back_populates="favorited_by")

    # Define the __repr__ method for representing User instances
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

    # Define the __str__ method for displaying usernames
    def __str__(self):
        return self.username

class Movie(db.Model):
    """ Define the Movie class as a subclass of Base (declarative_base).
    Defines columns for the movie table: movie_id (primary key), title, director, release_year, rating."""

    __tablename__ = 'movies'

    movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # primary key, autoincrement
    title = db.Column(db.String(255), nullable=False)  # stores the movie's title
    director = db.Column(db.String(100), nullable=False)  # stores the movie's director
    release_year = db.Column(db.Integer, nullable=False)  # stores the movie's release year
    rating = db.Column(db.Float, nullable=False)  # stores the movie's rating

    # Define the relationship with favorited_by
    favorited_by = db.relationship("User", secondary="user_movie",
                                   back_populates="favorite_movies")

    # Define the __repr__ method for representing Movie instances
    def __repr__(self):
        return f"<Movie(movie_id={self.movie_id}, title='{self.title}', director='{self.director}')>"

    # Define the __str__ method for displaying movie titles
    def __str__(self):
        return self.title


class UserMovie(db.Model):
    """ Define the UserMovie class as a subclass of Base (declarative_base).
    Defines columns for the user_movie table: ID (primary key), UserID (foreign key), MovieID (foreign key)."""

    __tablename__ = 'user_movie'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # primary key, autoincrement
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # foreign key referencing UserID in Users table
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), nullable=False)  # foreign key referencing MovieID in Movies table

    # Remove the back_populates arguments from relationships
    user = db.relationship("User")
    movie = db.relationship("Movie")

    # Define the __repr__ method for representing UserMovie instances
    def __repr__(self):
        return f"<UserMovie(id={self.id}, user_id={self.user_id}, movie_id={self.movie_id})>"

    # Define the __str__ method for displaying user-movie relationships
    def __str__(self):
        return f"User {self.user_id} marked Movie {self.movie_id} as a favorite"


class Review(db.Model):
    """ Define the Review class to store user reviews of movies. """

    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # primary key, autoincrement
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # foreign key referencing UserID in Users table
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), nullable=False)  # foreign key referencing MovieID in Movies table
    review_text = db.Column(db.Text, nullable=False)  # stores the user's review text

    user = db.relationship("User")
    movie = db.relationship("Movie")

    def __repr__(self):
        return f"<Review(review_id={self.review_id}, user_id={self.user_id}, movie_id={self.movie_id})>"

    def __str__(self):
        return f"Review {self.review_id}: User {self.user_id} - Movie {self.movie_id}\nReview Text: {self.review_text}"





