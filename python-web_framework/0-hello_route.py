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
# - strict_slashes=False allows for both "/path" and "path" URLs
# -----------------------------------------------------------------------------
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Return the string "Hello HBNB!" as the response to requests for the root path.
    """
    return "Hello HBNB!"

# -----------------------------------------------------------------------------
# Run the Flask application if the script is executed directly
# - host="0.0.0.0" makes the server accessible from external machines
# - port=5000 specifies the port number for the server to listen on
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
