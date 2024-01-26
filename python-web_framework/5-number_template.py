# -----------------------------------------------------------------------------
# Import the Flask module to create and manage the web application
# Import the render_template function for rendering HTML templates
# -----------------------------------------------------------------------------
from flask import Flask, render_template

# -----------------------------------------------------------------------------
# Create an instance of the Flask application
# -----------------------------------------------------------------------------
app = Flask(__name__)

# -----------------------------------------------------------------------------
# ... other routes (same as before) ...
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Define a route for paths starting with "/number_template/" and capture an integer value
# Render an HTML template using the captured value
# -----------------------------------------------------------------------------
@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Process paths starting with "/number_template/" and capture an integer value as "n".
    Render the "5-number.html" template, passing the captured value as "number" to the template context.
    """
    return render_template("5-number.html", number=n)

# -----------------------------------------------------------------------------
# Run the Flask application if the script is executed directly
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
