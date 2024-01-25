"""
Extended Flask Web Application

This module defines an extended Flask web application with multiple routes.

Usage:
- Run the script to start the web application.
- Access the following routes:
  - http://0.0.0.0:5000/ : Displays "Hello HBNB!"
  - http://0.0.0.0:5000/hbnb : Displays "HBNB"
  - http://0.0.0.0:5000/c/<text> : Displays "C " followed by the value of the text variable.
  - http://0.0.0.0:5000/python/<text> : Displays "Python " followed by the value of the text variable (default is "is cool").

Note:
- The application runs on 0.0.0.0, port 5000.
- The route definitions use `strict_slashes=False` to allow access with or without a trailing slash.
"""

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Home Route

    Displays a greeting message "Hello HBNB!".

    Returns:
    str: Greeting message.
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    HBNB Route

    Displays "HBNB".

    Returns:
    str: "HBNB".
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    C Route

    Displays "C " followed by the value of the text variable.
    Replace underscore _ symbols with a space.

    Args:
    text (str): The text variable.

    Returns:
    str: Formatted text.
    """
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"

@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """
    Python Route

    Displays "Python " followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    If no text is provided, the default is "is cool".

    Args:
    text (str): The text variable.

    Returns:
    str: Formatted text.
    """
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"

@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """
    Number Route

    Displays "n is a number" only if n is an integer.

    Args:
    n (int): The number variable.

    Returns:
    str: Formatted message.
    """
    if isinstance(n, int):
        return f"{n} is a number"
    else:
        return "Not a number"
    

if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
 