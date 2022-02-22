from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome"


@app.route('/home')
def welcome_home():
    return "welcome home"


@app.route('/back')
def welcome_back():
    return "welcome back"


