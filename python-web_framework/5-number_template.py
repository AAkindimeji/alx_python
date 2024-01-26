from flask import Flask, render_template

app = Flask(__name__)

# ... other routes (same as before) ...

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", number=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
