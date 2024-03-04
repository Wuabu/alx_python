import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    all_users_data = {}

    # Fetch data for all users
    for user_id in range(1, 11):
        user_url = "{}/{}".format(base_url, user_id)
        tasks_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)

        # Fetch user data
        user_response = requests.get(user_url)
        user_data = user_response.json()
        username = user_data.get('username')

        # Fetch tasks data
        tasks_response = requests.get(tasks_url)
        tasks_data = tasks_response.json()

        # Prepare JSON data for the specific user
        user_tasks = [{"username": username, "task": task["title"], "completed": task["completed"]} for task in tasks_data]
        all_users_data[str(user_id)] = user_tasks

    # Write data to todo_all_employees.json
    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        file.write(json.dumps(all_users_data, indent=2))

    print("Data for all employees saved to {}".format(filename))
