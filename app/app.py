import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/profile2')
def profile2():
    return render_template('profile2.html', name="John Doe", interests="production engineering!", location="New York, NY, USA", url=os.getenv("URL"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
    