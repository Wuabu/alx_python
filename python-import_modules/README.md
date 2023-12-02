Python Import Modules
This repository contains Python scripts showcasing the use of import statements and working with modules.

Table of Contents
Import a Simple Function
How to Make a Script Dynamic!
Everything Can Be Imported
Integers Division with Debug
Raise Exception
Raise a Message


Import a Simple Function

Task:
Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3.

Instructions:

Use the print function with string format to display integers.
Assign the value 1 to a variable called a and the value 2 to a variable called b.
Use those two variables as arguments when calling the functions add and print.
a and b must be defined in 2 different lines: a = 1 and b = 2.
Your program should print: <a value> + <b value> = <add(a, b) value> followed by a new line.
You can only use the word add_0 once in your code.
You are not allowed to use * for importing or __import__.
Your code should not be executed when imported - by using __import__.
Usage:



How to Make a Script Dynamic!

Task:
Write a program that prints the number of and the list of its arguments.

Instructions:

The output should be:
"Number of argument(s)" followed by "argument" (if the number is one) or "arguments" (otherwise), followed by : (or . if no arguments were passed), followed by a new line.
If at least one argument is provided, one line per argument:
The position of the argument (starting at 1) followed by :, followed by the argument value and a new line.
Your code should not be executed when imported.
The number of elements of argv can be retrieved by using len(argv).
You do not have to fully understand lists yet; imagine that argv can be used just like a collection of arguments.
Usage:



Everything Can Be Imported
Task:
Write a program that imports the variable a from the file variable_load_2.py and prints its value.

Instructions:

You are not allowed to use * for importing or __import__.
Your code should not be executed when imported.



Integers Division with Debug

Task:
Write a function that divides two integers and prints the result.

Instructions:

Prototype: def safe_print_division(a, b):
You can assume that a and b are integers.
The result of the division should print on the finally: section preceded by "Inside result:".
Returns the value of the division; otherwise: None.
Use try: / except: / finally:.
Use "{}".format() to print the result.
You are not allowed to import any module.


Raise Exception

Task:
Write a function that raises a type exception.

Instructions:

Prototype: def raise_exception():
You are not allowed to import any module.
Usage:


Exception raised
Raise a Message

Task:
Write a function that raises a name exception with a message.

Instructions:

Prototype: def raise_exception_msg(message=""):
You are not allowed to import any module.