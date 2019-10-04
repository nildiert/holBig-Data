#!/usr/bin/python3
"""
starts a Flask web application
"""

import os
from flask import Flask, jsonify
from api.v1.views import app_views
from flask_cors import CORS
app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.errorhandler(404)
def handle_404(err):
    """status render template for json"""
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    """init of the flask app"""
    ip = '0.0.0.0'
    port = '5000'
    app.run(host=ip, port=port, threaded=True, debug=True)
