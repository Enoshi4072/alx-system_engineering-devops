#!/usr/bin/python3
"""A script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get('name')
    completed_tasks = [task for task in todos_data if task['completed']]
    total_tasks = len(todos_data)

    print("Employee {} is done with tasks({}/{:.0f}):".format(
        employee_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t{}".format(task['title']))
