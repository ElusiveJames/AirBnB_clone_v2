#!/usr/bin/python3
""" creating a flask app """
from flask import Flask
""" class Flask """

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Return Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Return HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
