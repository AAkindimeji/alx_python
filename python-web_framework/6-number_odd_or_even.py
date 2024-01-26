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
# Define a route for paths starting with "/number_odd_or_even/" and capture an integer value
# Determine whether the captured value is odd or even and render a template accordingly
# -----------------------------------------------------------------------------
@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Process paths starting with "/number_odd_or_even/" and capture an integer value as "n".
    Determine whether the captured value is even or odd using a conditional expression.
    Render the "6-number_odd_or_even.html" template, passing the captured value and its odd/even status to the template context.
    """
    even_or_odd = "even" if n % 2 == 0 else "odd"  # Determine odd/even
    return render_template("6-number_odd_or_even.html", number=n, even_or_odd=even_or_odd)

# -----------------------------------------------------------------------------
# Run the Flask application if the script is executed directly
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
