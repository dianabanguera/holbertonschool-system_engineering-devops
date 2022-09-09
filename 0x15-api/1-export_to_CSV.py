#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export
data in the CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todos = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()
    with open('{}.csv'.format(sys.argv[1]), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([sys.argv[1], user.get('username'),
                             task.get('completed'), task.get('title')])
