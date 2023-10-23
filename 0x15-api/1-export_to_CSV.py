import requests
import sys
import csv

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()

        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data.get('name')
        completed_tasks = [task for task in todos_data if task['completed']]

        # Create a CSV file for the user
        filename = f"{employee_id}.csv"
        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task in todos_data:
                csv_writer.writerow([employee_id, employee_name, str(task['completed']), task['title']])

        print(f"Data exported to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    get_employee_todo_progress(employee_id)
