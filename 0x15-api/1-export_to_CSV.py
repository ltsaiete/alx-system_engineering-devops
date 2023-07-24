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

    for todo in todos:
        if todo['completed']:
            print(f'\t {todo["title"]}')
    with open(f'{id}.csv', 'w') as f:
        writer = csv.writer(f)
        row = [str(id), user["name"], todo["completed"], todo["title"]]
        for todo in todos:
            writer.writerow(row)
