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
    """Displays the text HBHN in an h1 HTML tag.

    Returns:
        str: HTML formatted message
    """
    return "HBNB"

if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)