#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    
    user_url = f"{base_url}/users/{user_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")
    
    todos_url = f"{base_url}/todos"
    todos_response = requests.get(todos_url, params={"userId": user_id})
    todos_data = todos_response.json()

    json_data = {user_id: [
        {"task": t.get("title"), "completed": t.get("completed"), "username": username} for t in todos_data]}

    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump(json_data, jsonfile)
