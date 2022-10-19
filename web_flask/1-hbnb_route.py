#!/usr/bin/python3
"""
starts a Flask web application listening on any IP port 5000.
Routes: '/' -- Returns 'Hello HBNB'
        '/hbnb' -- Returns the string 'HBNB'
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Sends the string 'Hello BNB!' to the browser"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Returns the string "HBNB" to the browser"""
    return "HBNB"
if __name__ == "__main__":
    app.run(host="0.0.0.0")
