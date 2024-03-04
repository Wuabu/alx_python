import json
import requests
import sys

def todo_list_progress(employee_id):
    # ... (unchanged)

def write_to_json(employee_id, employee_name, todos_details):
    # ... (unchanged)

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Fetching employee general details and converting JSON
    employee_details = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_details.json()

    # Fetching employee todo list details and converting to JSON
    employee_todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todos_details = employee_todos.json()

    todo_list_progress(employee_id)
    write_to_json(employee_id, employee_data["name"], todos_details)
