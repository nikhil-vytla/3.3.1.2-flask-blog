import os
from flask import Flask, request, render_template, send_from_directory
from dotenv import load_dotenv
from .backgrounds import get_random_background
from .profileInfo import get_profile_data
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from . import db
# from app.db import get_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{table}'.format(
    user=os.getenv('POSTGRES_USER'),
    passwd=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    port=5432,
    table=os.getenv('POSTGRES_DB'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class UserModel(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"

@app.route('/')
def index():
    home_data = get_profile_data("data/home.json")
    return render_template('index.html',
                           title="Nikhil's Blog",
                           url=os.getenv("URL"),
                           random_background=get_random_background(),
                           home_data=home_data)

@app.route('/portfolio')
def portfolio():
    profile_data = get_profile_data("data/profile.json")

    return render_template('profile.html', profile_data=profile_data)

@app.route("/blog")
def blog():
    return "Hey! You've found my unfinished blog!"

@app.route("/health")
def health():
    return "Hey! You've found an unfinished page!"

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif UserModel.query.filter_by(username=username).first() is not None:
            error = f"User {username} is already registered."

        if error is None:
            new_user = UserModel(username, generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            return f"User {username} created successfully"
        else:
            return error, 418

    ## TODO: Return a register page
    register_data = get_profile_data("data/register.json")
    return render_template('register.html', register_data=register_data)

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        error = None
        user = UserModel.query.filter_by(username=username).first()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password.'

        if error is None:
            return "Login Successful", 200
        else:
            return error, 418

    ## TODO: Return a login page
    login_data = get_profile_data("data/login.json")
    return render_template('login.html', login_data=login_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
