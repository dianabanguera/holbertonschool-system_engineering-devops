#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data
in the JSON format.
Dictionary of list of dictionaries"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    with requests.session() as session:
        tasks = session.get(todos_url).json()
        users = session.get(user_url).json()

        data_id = {}

        for user in users:
            list_data = []
            for record in tasks:
                if record["userId"] == user["id"]:
                    TASK_COMPLETED_STATUS = record["completed"]
                    TASK_TITLE = record["title"]
                    USERNAME = user["username"]
                    data = {
                        "task": TASK_TITLE,
                        "completed": TASK_COMPLETED_STATUS,
                        "username": USERNAME
                    }
                    list_data.append(data)

            data_id.update({user["id"]: list_data})

        text_file = "todo_all_employees.json"
        with open(text_file, mode="w+", encoding="utf-8") as file:
            json.dump(data_id, file)
