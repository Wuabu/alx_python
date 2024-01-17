Certainly! Below is a sample README file for the provided tasks:

---

# Python Object-Relational Mapping (ORM) - MySQL

This repository contains Python scripts that interact with a MySQL database using the MySQLdb module. The scripts perform various tasks related to selecting and filtering data from the database.

## Task 0: Get All States

### Description

Write a script that lists all states from the database `hbtn_0e_0_usa`. The script should take three arguments: MySQL username, MySQL password, and database name. It should connect to a MySQL server running on localhost at port 3306.

### Execution

```bash
python3 0-select_states.py root root hbtn_0e_0_usa
```

### Example Output

```plaintext
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
```

## Task 1: Filter States

### Description

Write a script that lists all states with a name starting with 'N' (upper N) from the database `hbtn_0e_0_usa`. The script should take three arguments: MySQL username, MySQL password, and database name. It should connect to a MySQL server running on localhost at port 3306.

### Execution

```bash
./1-filter_states.py root root hbtn_0e_0_usa
```

### Example Output

```plaintext
(4, 'New York')
(5, 'Nevada')
```

## Task 2: Filter States by User Input

### Description

Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where the name matches the argument. The script should take four arguments: MySQL username, MySQL password, database name, and state name searched. It should connect to a MySQL server running on localhost at port 3306.

### Execution

```bash
./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
```

### Example Output

```plaintext
(2, 'Arizona')
```

## Task 3: SQL Injection...

### Description

The script from Task 2 is vulnerable to SQL injection. This task requires writing a safe version of the script that is protected against SQL injection. The script should take four arguments: MySQL username, MySQL password, database name, and state name searched. It should connect to a MySQL server running on localhost at port 3306.

### Execution

```bash
./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
```

### Example Output

```plaintext
(2, 'Arizona')
```

## Task 4: Cities by States

### Description

Write a script that lists all cities from the database `hbtn_0e_4_usa`. The script should take three arguments: MySQL username, MySQL password, and database name. It should connect to a MySQL server running on localhost at port 3306.

### Execution

```bash
./4-cities_by_state.py root root hbtn_0e_4_usa
```

### Example Output

```plaintext
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
```

---

This README provides an overview of each script, its purpose, and instructions for execution. The examples demonstrate how to run the scripts and the expected output.