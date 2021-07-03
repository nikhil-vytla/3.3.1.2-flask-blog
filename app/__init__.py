import os
from flask import Flask, request, render_template, send_from_directory
from dotenv import load_dotenv
from .backgrounds import get_random_background
from .profileInfo import get_profile_data
from . import db

app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)

@app.route('/')
def index():
    home_data = get_profile_data("data/home.json")
    return render_template('index.html',
                           title="MLH Fellow",
                           url=os.getenv("URL"),
                           random_background=get_random_background(),
                           home_data=home_data)

@app.route('/portfolio')
def portfolio():
    profile_data = get_profile_data("data/nikhil.json")

    return render_template('profile.html', profile_data=profile_data)

@app.route("/blog")
def blog():
    return "Hey! You've found my unfinished blog!"

@app.route("/health")
def health():
    return "Hey! You've found an unfinished page!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
