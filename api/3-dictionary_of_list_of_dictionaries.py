import json
import requests
import sys

def todo_list_progress(employee_data, todos_details):
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
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1]) 

    employee_details = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_details.json()

    employee_todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todos_details = employee_todos.json()

    todo_list_progress(employee_data, todos_details)
    write_to_json(employee_id, employee_data["name"], todos_details)
