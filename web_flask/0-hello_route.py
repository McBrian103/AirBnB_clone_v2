#!/usr/bin/python3
"""
starts a Flask web application listening on any IP port 5000.
Routes:  '/' ---Displays 'HBNB!'

"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Sends the string 'Hello BNB!' to the browser"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
