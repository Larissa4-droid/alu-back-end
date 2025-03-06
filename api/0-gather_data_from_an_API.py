#!/usr/bin/python3
"""
Fetch TODO list progress of an employee from a REST API.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if the script received an employee ID as a parameter
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Define the API URLs
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Employee not found")
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todos data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task["title"] for task in todos_data if task["completed"]]
    total_tasks = len(todos_data)
    done_tasks = len(completed_tasks)

    # Print the result in the required format
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

