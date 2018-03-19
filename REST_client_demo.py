#!python
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
# REST Client processes
#  calls on: rest_server_demo (needs to be running)

from flask import Flask, jsonify, abort, request, make_response, url_for
import requests
import json

import os
from datetime import datetime, date, time, timedelta
from flask_httpauth import HTTPBasicAuth

f_URL = "http://127.0.0.1:5000"
f_auth = ('testuser', 'python')


def add_task(title, description, done):
    headers = {
        'Content-Type': 'application/json',
    }
    # new tasks
    task = {
        'title': title,
        'description': description,
        'done': done
        }

    data = json.JSONEncoder().encode(task)

    response = requests.post(
            f_URL + '/todo/api/v1.0/tasks', auth=f_auth, headers=headers,
            data=data)
    print(response.text)
    data_r = json.JSONDecoder().decode(response.text)
    print(data_r)


def replace_task(id, title, description, done):
    headers = {
        'Content-Type': 'application/json',
    }
    # new tasks
    task = {
        'id': str(id),
        'title': title,
        'description': description,
        'done': done
        }

    data = json.JSONEncoder().encode(task)

    response = requests.put(
        f_URL + '/todo/api/v1.0/tasks/' + str(id), auth=f_auth,
        headers=headers, data=data)
    print(response.text)
    data_r = json.JSONDecoder().decode(response.text)
    print(data_r)


def del_task(id):
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.delete(
        f_URL + '/todo/api/v1.0/tasks/' + str(id), auth=f_auth,
        headers=headers)
    print(response.text)
    data_r = json.JSONDecoder().decode(response.text)
    print(data_r)


def get_task(id):
    headers = {
        'Content-Type': 'application/json',
    }
    if id == "*":
        response = requests.get(
            f_URL + '/todo/api/v1.0/tasks', auth=f_auth, headers=headers)
    else:
        response = requests.get(
            f_URL + '/todo/api/v1.0/tasks/' + str(id), auth=f_auth,
            headers=headers)

    print(response.text)
    data_r = json.JSONDecoder().decode(response.text)
    print(data_r)


def main():
    add_task(u'Buy groceries', u'Milk, Cheese, Pizza, Fruit, Tylenol', False)
    add_task(
        u'Learn Python', u'Need to find a good Python tutorial on the web',
        False)
    replace_task(
        2,
        u'Learn Python',
        u'Need to find another good Python tutorial on the web', False)
    del_task(1)
    get_task(2)
    get_task("*")

if __name__ == '__main__':
    main()
