#!/usr/bin/python3

"""using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys

r = requests.get(f'https://jsonplaceholder.typicode.com/todos')
todos = r.json()
r = requests.get(f'https://jsonplaceholder.typicode.com/users')
users = r.json()

dict = {}
users_dict = {}

for user in users:
    users_dict[user['id']] = user

for todo in todos:
    todo_data = {
        "username": users_dict[todo['userId']]['username'],
        "task": todo["title"],
        "completed": todo["completed"],
    }
    if dict.get(todo['userId']):
        dict[todo['userId']].append(todo_data)
    else:
        dict[todo['userId']] = [todo_data]

with open('todo_all_employees.json', 'w') as f:
    f.write(json.dumps(dict))
# "username": users["username"],
