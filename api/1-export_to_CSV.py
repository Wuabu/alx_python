import requests
import csv
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

def export_to_csv(employee_data, todos_data):
    user_id = employee_data['id']
    username = employee_data['username']
    
    csv_filename = f'{user_id}.csv'
import csv
import requests
import sys


employee_id = int(sys.argv[1]) 

#fetching employee general details
employee_details = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
employee_data = employee_details.json()

#fetching employee todo list details
employee_todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
todos_details = employee_todos.json()

def todo_list_progress(employee_id):
    
    #fetching employee name
    employee_name = employee_data["name"]
    
    #fetching employee total todo list length and completed tasks
    total_tasks = len(todos_details)
    completed_tasks = sum(1 for todo in todos_details if todo["completed"])
    
    #printing employee todo list progress          
    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))

    for todo in todos_details:
        if todo["completed"]:
            print(f"\t {todo['title']}")
            
    
def write_to_csv(employee_id, employee_name, todos_details):
     with open("USER_ID.csv", "w", newline="") as csvfile:
         fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
         
         writer.writeheader()
         for todo in todos_details:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS":str(todo['completed']),
                "TASK_TITLE": todo['title']
            })
        
if __name__ == "__main__":   
    todo_list_progress(employee_id)
    write_to_csv(employee_id, employee_data['name'], todos_details)
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos_data:
            csv_writer.writerow([user_id, username, str(task['completed']), task['title']])

    print(f'Data exported to {csv_filename}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        employee_data, todos_data = get_employee_data(employee_id)
        export_to_csv(employee_data, todos_data)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
