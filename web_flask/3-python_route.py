#!/usr/bin/python3
"""
starts a Flask web application listening on any IP port 5000.
Routes: '/' -- Returns 'Hello HBNB'
        '/hbnb' -- Returns the string 'HBNB'
        '/c/<text> -- Displays "C" ffollowed by the value of the text variable.
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


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Dispalys the string 'C' followed by the value of text variable."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """Displays the string 'Python" followed by the value of text variable.
       text variable defaults to 'cool'
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
