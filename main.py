#!/usr/bin/env python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
import os.path
import uuid
import random
from flask import Flask, request, render_template, \
    json, jsonify, redirect, url_for

# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

@app.route('/zonematchramdom', methods=['GET', 'POST'])
def zonematchramdom():
    """
    handles request to custom template with states, cities & amentities
    """
    data = request.get_json(silent=True)
    print("---------")
    print(data)
    print("---------")
    data = {"name":"Test", "lastname": "Test", "image":"https://avatars3.githubusercontent.com/u/2479899?s=460&v=4", "token": "testtoken"}
    return render_template('card.html', otherdata=data)


@app.route('/zonematch', methods=['GET', 'POST'])
def zonematch():
    """
    handles request to custom template with states, cities & amentities
    """
    data = request.get_json(silent=True)
    print("---------")
    print(data)
    print("---------")
    data = {"name":"Test", "lastname": "Test", "image":"https://avatars3.githubusercontent.com/u/2479899?s=460&v=4", "token": "testtoken"}
    return render_template('play.html', data=data)


@app.route('/login', methods=['GET'])
def login():
    """
    handles request to custom template with states, cities & amentities
    """
    return render_template('login.html')

@app.route('/', methods=['GET'])
def index():
    data = {"token":"", "cache_id":uuid.uuid4(),"title":"Sing In to play!"}
    return render_template('index.html', data=data)


if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
