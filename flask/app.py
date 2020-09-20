from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "hello"


def photo():
    return "photo.jpg"
