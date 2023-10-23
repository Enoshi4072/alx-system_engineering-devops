#!/usr/bin/python3
"""
Python script to export data in the JSON format.

Requirements:

Records all tasks that are owned by this employee
"""
import requests
import sys
import json

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch user information
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    username = user_data.get('username')

    # Fetch user's TODO list
    todo_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todo_data = todo_response.json()

    # Create a list of tasks
    tasks = []
    for task in todo_data:
        task_info = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username
        }
        tasks.append(task_info)

    # Create a JSON file with the user's tasks
    file_name = f'{employee_id}.json'
    with open(file_name, 'w') as json_file:
        json.dump({employee_id: tasks}, json_file)
