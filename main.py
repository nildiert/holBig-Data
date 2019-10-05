#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from flask import Flask, render_template, url_for
import uuid


# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'



@app.route('/login')
def login(the_id=None):
    """
    handles request to custom template with states, cities & amentities
    """
    return render_template('login.html')


if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)

