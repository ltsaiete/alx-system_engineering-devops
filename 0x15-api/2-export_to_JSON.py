#!/usr/bin/python3

"""using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys

if len(sys.argv) > 1:
    id = sys.argv[1]
    r = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={id}')
    todos = r.json()
    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    user = r.json()

    dict = {id: []}

    for todo in todos:
        dict[id].append(
            {"task": todo["title"],
             "completed": todo["completed"],
             "username": user["username"]}
        )

    with open(f'{id}.json', 'w') as f:
        f.write(json.dumps(dict))
