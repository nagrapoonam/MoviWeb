from flask import Blueprint, jsonify, request
from datamanager.sqlite_data_manager import SQLiteDataManager
from data_models import db,User, Movie, UserMovie, Review

api = Blueprint('api', __name__)

# Create an instance of SQLiteDataManager
data_manager = SQLiteDataManager(db)

@api.route('/users', methods=['GET'])
def get_users():
    users = data_manager.list_all_users()
    user_data = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify(user_data)


@api.route('/users/<int:user_id>/movies', methods=['GET'])
def get_user_movies(user_id):
    user_movies = data_manager.list_user_movies(user_id)
    if user_movies:
        movie_data = [{'id': movie.movie_id, 'title': movie.title, 'director': movie.director} for movie in user_movies]
        return jsonify(movie_data)
    else:
        return "User not found or has no favorite movies", 404

@api.route('/users/<int:user_id>/movies', methods=['POST'])
def add_user_movie(user_id):
    movie_data = request.get_json()
    title = movie_data.get('title')
    director = movie_data.get('director')
    release_year = movie_data.get('release_year')
    rating = movie_data.get('rating')

    new_movie = Movie(title=title, director=director, release_year=release_year, rating=rating)
    data_manager.add_movie(new_movie)

    user = data_manager.get_user_by_id(user_id)
    if user:
        user.favorite_movies.append(new_movie)
        data_manager.commit()

        return jsonify({"message": "Movie added to user's favorites successfully"})
    else:
        return "User not found", 404