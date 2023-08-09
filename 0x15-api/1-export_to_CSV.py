#!/usr/bin/python3

"""using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
import sys

if len(sys.argv) > 1:
    id = sys.argv[1]
    r = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={id}')
    todos = r.json()
    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    user = r.json()

    with open(f'{id}.csv', 'w') as f:
        writer = csv.writer(f)
        for todo in todos:
            row = [f"{id}", user["username"],
                   todo["completed"], todo["title"]]
            writer.writerow(row)
