#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ print hello hbnb """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ print hbnb """
    return 'HBNB'


@app.route('/c/<path:text>')
def c_route(text):
    """ print c followed by the given text """
    value = text.replace('_', ' ')
    return 'C {}'.format(value)


@app.route('/python')
@app.route('/python/<text>')
def python_route(text='is cool'):
    """ print python followed by the given text
    with default value of text: is cool """
    value = text.replace('_', ' ')
    return 'Python {}'.format(value)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
