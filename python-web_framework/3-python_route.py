# -----------------------------------------------------------------------------
# Import the Flask module to create and manage the web application
# -----------------------------------------------------------------------------
from flask import Flask

# -----------------------------------------------------------------------------
# Create an instance of the Flask application
# -----------------------------------------------------------------------------
app = Flask(__name__)

# -----------------------------------------------------------------------------
# Define a route for the root path ("/")
# -----------------------------------------------------------------------------
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Return the string "Hello HBNB!" as the response to requests for the root path.
    """
    return "Hello HBNB!"

# -----------------------------------------------------------------------------
# Define a route for the "/hbnb" path
# -----------------------------------------------------------------------------
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Return the string "HBNB" as the response to requests for the "/hbnb" path.
    """
    return "HBNB"

# -----------------------------------------------------------------------------
# Define a route for paths starting with "/c/" and capture a dynamic value
# -----------------------------------------------------------------------------
@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """
    Process paths starting with "/c/" and capture a dynamic value as "text".
    Replace underscores in "text" with spaces and return "C " followed by the modified text.
    """
    text = text.replace("_", " ")
    return f"C {text}"

# -----------------------------------------------------------------------------
# Define routes for both "/python/" and "/python/<text>" with a default value
# -----------------------------------------------------------------------------
@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """
    Handle requests for both "/python/" and "/python/<text>" paths.
    Replace underscores in "text" with spaces and return "Python " followed by the modified text.
    If no text is provided in the URL, use the default value "is cool".
    """
    text = text.replace("_", " ")
    return f"Python {text}"

# -----------------------------------------------------------------------------
# Run the Flask application if the script is executed directly
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
