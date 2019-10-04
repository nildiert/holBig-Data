#!/usr/bin/python3
"""function to create the route status"""
from api.v1.views import app_views
from flask import jsonify, abort, request
import requests
import json


@app_views.route('/')
def root():
    return jsonify({"Hola": "OK"})

@app_views.route('/auth_token')
def get_auth_token():
    student = {
        "api_key": request.form.get('api_key'),
        "email": request.form.get('email'),
        "password": request.form.get('password'),
        "scope": "checker"
    }

    res = requests.post('https://intranet.hbtn.io/users/auth_token.json', data=student)

    return jsonify(token= res.json()["auth_token"])

@app_views.route('/love_path_photo')
def love_path_photo():
    auth_token = {"auth_token": token}
    headers = {'Content-Type': 'application/json'}
    res = requests.get('https://intranet.hbtn.io/users/me.json', params=auth_token, headers=headers)
    return res.json()
