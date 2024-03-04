# Import necessary modules
import requests
import json
import sys

def get_employee_data(employee_id):
    """
    Fetches employee details and their TODO list from the JSONPlaceholder API.

    Parameters:
        employee_id (int): The ID of the employee for whom data is to be fetched.

    Returns:
        tuple: A tuple containing the employee details and their TODO list.
    """
    # Fetch employee details
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response_employee = requests.get(employee_url)
    employee_data = response_employee.json()

    # Fetch TODO list for the employee
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response_todos = requests.get(todos_url)
    todos_data = response_todos.json()

    return employee_data, todos_data

def export_to_json(employee_data, todos_data):
    """
    Exports employee's TODO list data to a JSON file.

    Parameters:
        employee_data (dict): Details of the employee.
        todos_data (list): List of TODO items for the employee.
    """
    user_id = employee_data['id']
    username = employee_data['username']
    
    json_filename = f'{user_id}.json'

    tasks_list = [{"task": task['title'], "completed": task['completed'], "username": username} for task in todos_data]
    data_to_export = {str(user_id): tasks_list}

    with open(json_filename, 'w') as json_file:
        json.dump(data_to_export, json_file, indent=2)

    print(f'Data exported to {json_filename}')

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command-line arguments
    employee_id = int(sys.argv[1])

    try:
        # Fetch employee data and TODO list
        employee_data, todos_data = get_employee_data(employee_id)
        
        # Export data to JSON file
        export_to_json(employee_data, todos_data)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
