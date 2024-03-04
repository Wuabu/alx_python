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

def todo_list_progress(employee_id):
    '''
    Retrieves the todo list progress of an employee and writes it to a JSON file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    '''
    # Fetching employee general details and converting JSON
    employee_details = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_details.json()

    # Fetching employee todo list details and converting to JSON
    employee_todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todos_details = employee_todos.json()

    # Fetching employee name from general details
    employee_name = employee_data["name"]

    # Fetching employee total todo list length and completed tasks
    total_tasks = len(todos_details)
    completed_tasks = sum(1 for todo in todos_details if todo["completed"])

    # Printing employee todo list progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))

    for todo in todos_details:
        if todo["completed"]:
            print(f"\t {todo['title']}")

def write_to_json(employee_id, employee_name, todos_details):
    """
    Writes employee todo list details to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The name of the employee.
        todos_details (list): List containing todo details.

    Returns:
        None
    """
    response = {str(employee_id): [{"task": todo["title"], "completed": todo["completed"], "username": employee_name} for todo in todos_details]}
    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(response, json_file, indent=4)

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    todo_list_progress(employee_id)
    write_to_json(employee_id, employee_data["name"], todos_details)