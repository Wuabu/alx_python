"""
Writes employee todo list details to a JSON file.

Args:
    employee_id (int): The ID of the employee.
    employee_name (str): The name of the employee.
    todos_details (list): List containing todo details.

Returns:
    None
"""
import json
import requests
import sys
'''
    Retrieves the todo list progress of an employee and writes it to a JSON file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    '''
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
