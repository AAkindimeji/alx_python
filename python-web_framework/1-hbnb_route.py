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
# Run the Flask application if the script is executed directly
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
