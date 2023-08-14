from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datamanager.sqlite_data_manager import SQLiteDataManager
from data_models import db,User, Movie, UserMovie

app = Flask(__name__)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/User/PycharmProjects/SE107.3/MoviWeb/data/moviwebapp.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy()
db.init_app(app)

# db = SQLAlchemy(app)  # Initialize SQLAlchemy with the app

data_manager = SQLiteDataManager(app)  # Pass the app directly here

@app.route('/')
def index():
    users = data_manager.list_all_users()
    return render_template('index.html', users=users)
    # return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


#create the database tables
# with app.app_context():
#     db.create_all()