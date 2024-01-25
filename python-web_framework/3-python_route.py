"""
Simple Flask Web Application

This module defines a simple Flask web application with multiple routes.

Usage:
- Run the script to start the web application.
- Access the home route at http://0.0.0.0:5000/ in a web browser or using curl.

Routes:
- `/`: Displays a greeting message "Hello HBNB!" in an h1 HTML tag.
- `/hbnb`: Displays "HBNB".
- `/c/<text>`: Displays "C " followed by the value of the text variable (replace underscore _ symbols with a space).

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

    Displays a greeting message "Hello HBNB!" in an h1 HTML tag.

    Returns:
    str: HTML-formatted greeting message.
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

@app.reoute("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    
    """Python Route

    Displays "Python " followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    If no text is provided, the default is "is cool".

    Args:
    text (str): The text variable.

    Returns:
    str: Formatted text.
    """
    formatted_text = text.replace('_',' ')
    return f"Python {formatted_text}"

if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
