#!/usr/bin/python3
"""Returns information about user to-do list progress using employee ID."""
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + f'users/{sys.argv[1]}')
    todos = requests.get(url + 'todos', params={'userId': sys.argv[1]})

    name = users.json().get('name')
    completed = []
    for task in todos.json():
        if task.get('completed') is True:
            completed.append(task.get('title'))

    print(f'Employee {name} is done with tasks\
            ({len(completed)}/{len(todos.json())})')
    [print(f'\t {title}') for title in completed]
