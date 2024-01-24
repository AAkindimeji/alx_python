from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    text = text.replace("_", " ")
    return f"C {text}"

@app.route("/python/<text>", defaults={'text': 'is cool'}, strict_slashes=False)
def python_text(text):
    text = text.replace("_", " ")
    return f"Python {text}"

@app.route("/number/<n>", strict_slashes=False)
def number(n):
    if n.isdigit():
        return f"{n} is a number"
    else:
        return "Not a number", 404

@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    if n.isdigit():
        return render_template("number_template.html", number=n)
    else:
        return "Not a number", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
