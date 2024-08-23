#!/usr/bin/python3
""" creating a flask app """
from flask import Flask, abort
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


@app.route('/python/', strict_slashes=False)
def python_default():
    return "Python is cool"


@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    try:
        int(n)
        return "{} is a number".format(n)
    except ValueError:
        abort(404)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
