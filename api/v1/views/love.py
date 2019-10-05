#!/usr/bin/python3
"""function to create the route status"""
from api.v1.views import app_views
from flask import jsonify, abort, request, Response
import requests
import json
import random
import time


projects = {
    "0-Day - 0-Day":["210", "206", "211"],
    "Higher-level programming":[
        "231", "233", "239", "241", "243",
        "245", "247", "246", "250", "252",
        "254", "260", "331", "283", "299",
        "300", "303", "304", "333", "305",
        "272", "274", "263", "268", "289",
        "288", "290", "301"],
    "Low-level programming":[
        "213","212","214","215","216","217",
        "218","219","220","221","222","223",
        "225","224","226","227","228","232",
        "242","273","229","230","240","249",
        "253","248","270","295","234","235"],
    "System engineering & DevOps":[
        "205","207","208","209","251","255",
        "269","314","259","285","302","266",
        "275","276","298","280","281","244",
        "284","292","265","271","287"]
}


@app_views.route('/')
def root():
    ret = '{"data": "JSON string example"}'

    resp = Response(response=ret,
                    status=200,
                    mimetype="application/javascript")

    return jsonify(status= "OK!")


@app_views.route('/auth_token', methods=['POST'])
def get_auth_token():
    student = {
        "api_key": "13278f54bc616165bf99889881d0ba3a",
        "email": "792@holbertonschool.com",
        "password": "keepitsimple123++",
        "scope": "checker"
    }

    res = requests.post('https://intranet.hbtn.io/users/auth_token.json', data=student)

    return jsonify(token= res.json()["auth_token"])

@app_views.route('/love_path_photo')
def love_path_photo():
    auth_token = {"auth_token": token}
    headers = {
        'Content-Type': 'application/json',
    }
    res = requests.get('https://intranet.hbtn.io/users/me.json', params=auth_token, headers=headers)
    return res.json()

@app_views.route('/task')
def task():
    #get a project
    auth_token = {"auth_token": '2a1add613f04e5f95f227ffa1c71e68d4df29ee8fe6a13acb0ef286a81f084c1'}
    headers = {
        'Content-Type': 'application/json',

    }
    task_list = random.choice(list(projects.values()))
    task = random.choice(task_list)
    res = requests.get('https://intranet.hbtn.io/projects/{}.json'.format(task), params=auth_token, headers=headers)

    proj = res.json()
    proj_tasks = proj["tasks"]
    #last_task = proj_tasks[len(proj_tasks) - 1]
    last_task = random.choice(proj_tasks)

    #get a correction
    correction = requests.post('https://intranet.hbtn.io/tasks/{}/start_correction.json'.format(last_task["id"]), data=auth_token)
    task_id = correction.json()["id"]

    #get a correction result
    task_checks = requests.get('https://intranet.hbtn.io/correction_requests/{}.json'.format(task_id), params=auth_token, headers=headers)
    while (task_checks.json()["status"] == "Sent"):
        time.sleep(3)
        task_checks = requests.get('https://intranet.hbtn.io/correction_requests/{}.json'.format(task_id), params=auth_token, headers=headers)
    # check if all checkers of the tasks have passed
    results = task_checks.json()['result_display']
    dict_task = {"title": last_task["title"],
                 "repo": last_task["github_repo"],
                 "file": last_task["github_file"],
                 "status": "Done, You are ready to love"
    }
    for check in results["checks"]:
        if check["passed"] == False:
            dict_task["status"] = "Not 100%, You are NOT ready to love"
    return dict_task
