Employee TODO List Progress Script
This Python script utilizes the given REST API to fetch information about a specific employee's TODO list progress. It accepts an employee ID as a parameter and displays the progress in the specified format.

Requirements
The script uses the requests module to make API requests.
The employee ID is provided as a command-line argument.
Installation
Ensure you have the requests module installed:

bash
Copy code
pip install requests
Usage
Run the script from the command line with the employee ID as an argument:

bash
Copy code
python script.py <employee_id>
Replace <employee_id> with the desired employee's ID.

Example
bash
Copy code
python script.py 2
Output
The script will output information about the employee's TODO list progress in the specified format:

csharp
Copy code
Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    TASK_TITLE_1
    TASK_TITLE_2
    ...
    TASK_TITLE_N
Note
Replace EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS, and TASK_TITLE with actual values fetched from the API.
Feel free to modify and extend the script based on your requirements.