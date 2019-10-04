from flask import request, jsonify

from app import create_app
from projects import projects

app = create_app()

@app.route('/')
def index():
    return jsonify({"key":projects})