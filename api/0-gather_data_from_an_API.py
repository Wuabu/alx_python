import requests
import sys

def get_employee_data(employee_id):
    # Fetch employee details
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response_employee = requests.get(employee_url)
    employee_data = response_employee.json()
    
    # Fetch TODO list for the employee
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response_todos = requests.get(todos_url)
    todos_data = response_todos.json()
    
    return employee_data, todos_data

def display_todo_progress(employee_data, todos_data):
    employee_name = employee_data['name']
    
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    
    try:
        employee_data, todos_data = get_employee_data(employee_id)
        display_todo_progress(employee_data, todos_data)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
