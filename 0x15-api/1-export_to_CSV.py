#!/usr/bin/python3
import requests
import sys
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos".format(base_url)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url, params={"userId": employee_id})

    user_data = user_response.json()
    todos_data = todos_response.json()
    employee_name = user_data.get('name')

    # Create a CSV file for the user with values enclosed in double quotes
    filename = "{}.csv".format(employee_id)
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        [csv_writer.writerow(
            [str(employee_id), employee_name, str(
                task['completed']), task['title']]) for task in todos_data]
