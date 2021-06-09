import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv
from .backgrounds import get_random_background
load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           title="MLH Fellow",
                           url=os.getenv("URL"),
                           random_background=get_random_background())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
    