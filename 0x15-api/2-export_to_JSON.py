#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export
data in the JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todos = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()
    username = user.get('username')
    tasks = []  # list of tasks
    for task in todos:
        tasks.append({"task": task.get('title'),
                      "completed": task.get('completed'),
                      "username": username})
    jsonobj = {sys.argv[1]: tasks}
    jsonobj[sys.argv[1]] = tasks
    with open('{}.json'.format(sys.argv[1]), 'w') as jsonfile:
        json.dump(jsonobj, jsonfile)
