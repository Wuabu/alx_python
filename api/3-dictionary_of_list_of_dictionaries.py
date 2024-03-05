"""
Records all employee tasks as a dictionary to a JSON file.

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

def todo_list_progress():
    global employee_data
    global todos_details

    employee_name = employee_data["name"]
    
    total_tasks = len(todos_details)
    completed_tasks = sum(1 for todo in todos_details if todo["completed"])
    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))

    for todo in todos_details:
        if todo["completed"]:
            print(f"\t {todo['title']}")

def employee_tasks_record(employee_name, todos_details):
    employee_tasks = [{"username": employee_name, "task": todo["title"], "completed": todo["completed"]} for todo in todos_details]
    return employee_tasks

def write_to_json(employee_id, employee_name, todos_details):
    all_employees_tasks = {str(employee_id): employee_tasks_record(employee_name, todos_details)}
    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(all_employees_tasks, json_file, indent=4)

if __name__ == "__main__":
    employee_id = int(sys.argv[1]) 

    employee_details = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_details.json()

    employee_todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todos_details = employee_todos.json()

    todo_list_progress()
    write_to_json(employee_id, employee_data["name"], todos_details)