#!/usr/bin/python3
""" ok """

from flask import Flask
from urllib.parse import unquote

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<path:text>', strict_slashes=False)
def c_route(text):
    value = unquote(text.replace('_', ' '))
    return 'C {}'.format(value)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
