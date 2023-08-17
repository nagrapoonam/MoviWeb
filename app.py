from flask import Flask, render_template, request, redirect, url_for, make_response
from datamanager.sqlite_data_manager import SQLiteDataManager
from data_models import db,User, Movie, Review
from MoviWeb.api import api  # Importing the API blueprint






app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')  # Registering the blueprint

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/User/PycharmProjects/SE107.3/MoviWeb/data/moviwebapp.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db.init_app(app)



data_manager = SQLiteDataManager(db)  # Pass the app directly here







@app.route('/')
def index():
    users = data_manager.list_all_users()
    return render_template('index.html', users=users)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        new_user = User(username=username, email=email, password=password)
        data_manager.add_user(new_user)

        return redirect(url_for('index'))

    return render_template('add_user.html')


@app.route('/list_users')
def list_users():
    users = data_manager.list_all_users()
    return render_template('list_users.html', users=users)


@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form.get('title')
        director = request.form.get('director')
        release_year = int(request.form.get('release_year'))
        rating = float(request.form.get('rating'))

        new_movie = Movie(title=title, director=director,
                          release_year=release_year, rating=rating)
        data_manager.add_movie(new_movie)

        return redirect(url_for('list_movies'))

    return render_template('add_movie.html')


@app.route('/update_movie/<int:movie_id>', methods=['GET', 'POST'])
def update_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        return "Movie not found", 404

    if request.method == 'POST':
        title = request.form.get('title')
        director = request.form.get('director')
        release_year = int(request.form.get('release_year'))
        rating = float(request.form.get('rating'))

        movie.title = title
        movie.director = director
        movie.release_year = release_year
        movie.rating = rating

        data_manager.update_movie(movie)

        return redirect(url_for('list_movies'))

    return render_template('update_movie.html', movie=movie)


@app.route('/delete_movie/<int:movie_id>', methods=['POST'])
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        return "Movie not found", 404

    data_manager.delete_movie(movie_id)

    return redirect(url_for('list_movies'))


@app.route('/list_movies')
def list_movies():
    movies = Movie.query.all()
    return render_template('list_movies.html', movies=movies)


@app.route('/add_review', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        user_id = int(request.form.get('user_id'))
        movie_id = int(request.form.get('movie_id'))
        review_text = request.form.get('review_text')

        # Create a new Review instance
        new_review = Review(user_id=user_id, movie_id=movie_id, review_text=review_text)

        # Add the new review to the database
        db.session.add(new_review)
        db.session.commit()

        return redirect(url_for('list_reviews'))  # Redirect to list_reviews with movie_id

    # If it's a GET request, render the add_review.html template
    return render_template('add_review.html')


@app.route('/list_reviews')
def list_reviews():
    reviews = data_manager.list_all_reviews()  # Modify this method accordingly
    return render_template('list_review.html', reviews=reviews)


@app.route('/delete_review/<int:review_id>', methods=['GET', 'POST'])
def delete_review(review_id):
    if request.method == 'POST':
        review = data_manager.get_review_by_id(review_id)
        if review:
            data_manager.delete_review(review)
            message = "Review deleted successfully."
        else:
            message = "Review not found."

    reviews = data_manager.list_all_reviews()  # You need to modify this method accordingly
    return render_template('list_review.html', reviews=reviews,
                           message=message)





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


#create the database tables
with app.app_context():
    db.create_all()