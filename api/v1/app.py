#!/usr/bin/python3
"""
starts a Flask web application
"""

import os
from flask import Flask, request, jsonify, render_template, redirect, make_response, session
from api.v1.views import app_views
from flask_cors import CORS
from .config import Config

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}});


@app.errorhandler(404)
def handle_404(err):
    """status render template for json"""
    return jsonify({"error": "Not found"}), 404

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/login'))
    session['user_ip'] = user_ip
    return  response
    #jsonify({"key":projects})


if __name__ == '__main__':
    """init of the flask app"""
    ip = '0.0.0.0'
    port = '5001'
    app.config['SECRET_KEY'] = 'SUPER SECRETO'
    app.config.from_object(Config)
    app.run(host=ip, port=port, threaded=True, debug=True)
