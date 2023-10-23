#!/usr/bin/python3
"""Export data from the JSONPlaceholder API and store it in JSON format."""
import json
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 1:
        sys.exit()

    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    response_users = requests.get(url_users)
    response_todos = requests.get(url_todos)

    try:
        users = response_users.json()
        todos = response_todos.json()
    except ValueError:
        sys.exit()

    user_dict = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_dict[user_id] = []

    for task in todos:
        task_dict = {
            "username": username,
            "task": task['title'],
            "completed": task['completed']
        }
        user_dict[task['userId']].append(task_dict)

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_dict, json_file)
