from flask import Flask, render_template

app = Flask(__name__)

# ... other routes (same as before) ...

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    even_or_odd = "even" if n % 2 == 0 else "odd"  # Determine odd/even
    return render_template("6-number_odd_or_even.html", number=n, even_or_odd=even_or_odd)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
