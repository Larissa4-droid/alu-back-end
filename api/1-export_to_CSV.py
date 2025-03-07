#!/usr/bin/python3
"""
Fetch TODO list progress of an employee and export to CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    # Check if the script received an employee ID as a parameter
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Define API URLs
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Employee not found")
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch todos data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Define CSV file name
    file_name = f"{employee_id}.csv"

    # Write to CSV file
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, username, task["completed"], task["title"]])

    print(f"Data exported to {file_name}")

