#!/usr/bin/python3
"""function to create the route status"""
from api.v1.views import app_views
from flask import jsonify, abort, request
import requests



@app_views.route('/')
def root():
    return jsonify({"Hola": "OK"})

@app_views.route('/love_path_photo')
def love_path_photo():
    auth_token = {"auth_token": "1b565e64dcf1e8ca5ec38900ca29d15a7871e65cf2bcb71caad153609e1c6d67"}
    headers = {'Content-Type': 'application/json'}
    res = requests.get('https://intranet.hbtn.io/users/me.json', params=auth_token, headers=headers)
    return res.json()
