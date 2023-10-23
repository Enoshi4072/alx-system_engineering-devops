#!/usr/bin/python3
"""  script that, using this REST API, for a
given employee ID, returns information
about his/her TODO list progress. """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    base_url = "https://jsonplaceholder.typicode.com/todos"

    # Get the list of all todos for the given employee ID
    response = requests.get(base_url, params={"userId": employee_id})
    todos = response.json()

    # Filter completed and total tasks
    completed_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)

    # Get the employee's name
    user_response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    employee_name = user_response.json()['name']

    # Print the progress report
    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t{}".format(task['title']))
