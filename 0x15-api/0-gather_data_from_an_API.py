#!/usr/bin/python3

"""using this REST API, for a given employee ID,
   returns information about his/her TODO list progress.
"""
import requests
import sys

id = sys.argv[1]

r = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={id}')
todos = r.json()
r = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
user = r.json()

done = 0
total = len(todos)

for todo in todos:
    if todo['completed']:
        done = done + 1

print(f'Employee {user["name"]} is done with tasks({done}/{total}):')

for todo in todos:
    if todo['completed']:
        print(f'\t{todo["title"]}')
