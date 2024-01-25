"""
Simple Flask Web Application

This module defines a simple Flask web application with one route.

Usage:
- Run the script to start the web application.
- Access the home route at http://0.0.0.0:5000/ in a web browser or using curl.

Routes:
- `/`: Displays a greeting message "Hello HBNB!" in an h1 HTML tag.

Note:
- The application runs on 0.0.0.0, port 5000.
- The route definition uses `strict_slashes=False` to allow access with or without a trailing slash.
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

if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
