from flask import Flask, request, render_template

app = Flask(__name__)

# ... previous routes ...

@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n):
    if not n.isdigit():
        return "Not a number", 404

    number = int(n)
    odd_or_even = "even" if number % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", number=number, odd_or_even=odd_or_even)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
