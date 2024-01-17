#!/usr/bin/python3
import MySQLdb
import sys

def my_safe_filter_states(username, password, db_name, search_name):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    
    # Execute the SQL query with the user input as a parameter
    cursor.execute(query, ('%' + search_name + '%',))

    # Fetch all rows from the result set
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command-line arguments
    username, password, db_name, search_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Call the function to filter states safely
    my_safe_filter_states(username, password, db_name, search_name)
