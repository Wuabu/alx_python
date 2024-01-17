#!/usr/bin/python3
import MySQLdb
import sys

def cities_by_state(username, password, db_name, state_name):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    # Execute the SQL query with the user input as a parameter
    cursor.execute(query, (state_name,))

    # Fetch all rows from the result set
    cities = cursor.fetchall()

    # Display the results
    for city in cities:
        print(city)

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command-line arguments
    username, password, db_name, state_name = sys.argv[
