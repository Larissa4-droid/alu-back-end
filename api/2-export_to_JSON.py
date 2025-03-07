#!/usr/bin/python3
"""
Fetch TODO list progress of an employee and export to JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Employee not found")
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get("username")

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    tasks_list = [
        {"task": task["title"], "completed": task["completed"],
         "username": username}
        for task in todos_data
    ]

    json_data = {str(employee_id): tasks_list}
    file_name = f"{employee_id}.json"

    with open(file_name, "w") as json_file:
        json.dump(json_data, json_file)

    print(f"Data exported to {file_name}")
