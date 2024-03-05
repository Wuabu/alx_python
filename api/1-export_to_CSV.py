import csv
import requests
import sys
import os  # Import the os module to check if the file exists

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

def export_to_csv(employee_data, todos_data):
    user_id = employee_data['id']
    username = employee_data['username']
    
    csv_filename = f'{user_id}.csv'
    
    with open(csv_filename, "w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for todo in todos_data:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": str(todo['completed']),
                "TASK_TITLE": todo['title']
            })

    print(f'Data exported to {csv_filename}')

def count_tasks_in_csv(user_id):
    csv_filename = f'{user_id}.csv'

    # Check if the file exists
    if os.path.exists(csv_filename):
        with open(csv_filename, 'r') as f:
            # Use csv.reader to read the CSV file
            reader = csv.reader(f)
            
            # Subtract 1 for the header row
            num_tasks = sum(1 for row in reader) - 1
            print(f'Number of tasks in CSV: {num_tasks}')
    else:
        print(f'CSV file not found: {csv_filename}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        employee_data, todos_data = get_employee_data(employee_id)
        export_to_csv(employee_data, todos_data)
        count_tasks_in_csv(employee_id)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
