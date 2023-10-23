#!/usr/bin/python3
"""
 Python script that, using this REST API,
 for a given employee ID, returns information
 about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch user information
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch user's TODO list
    todo_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todo_data = todo_response.json()

    # Calculate the number of done and total tasks
    total_tasks = len(todo_data)
    done_tasks = sum(1 for task in todo_data if task.get('completed'))

    # Display employee's progress
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in todo_data:
        if task.get('completed'):
            print(f"\t {task.get('title')}")
