#!/usr/bin/python3
"""
starts a Flask web application listening on any IP port 5000.
Routes: '/' -- Returns 'Hello HBNB'
        '/hbnb' -- Returns the string 'HBNB'
        '/c/<text> -- Displays "C" ffollowed by the value of the text variable.
        '/python/<text> -- Displays "Python" followed by the value of the text
                           variable.
        '/number/<n> -- Displays 'n is a number' if n is an integer.
        '/number_template/<n> -- displays a html page only if n is an integer.
        '/number_odd_or_even/<n> -- Displays HTML page only if n is an integer

"""
from flask import Flask
from flask import render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def is_integer(n):
    """Displays 'n is a number' only if n is an integer.
    """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Displays a HTML page only if n is an integer.
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """Displays a HTML page only if n is an integer.
       H1 content of rendered template is based on whether n is even or odd.
    """
    return render_template('6-number_odd_or_even.html', n=n)
if __name__ == "__main__":
    app.run(host="0.0.0.0")
