from flask import request, jsonify, render_template, redirect, make_response, session

from app import create_app
from projects import projects

app = create_app()

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/login'))
    session['user_ip'] = user_ip
    return  response
    #jsonify({"key":projects})


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/validate', methods=['POST'])
def validate():
    return request.form.get('user')
