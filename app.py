from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # basic security checks
    if not username or not password:
        return render_template("index.html", error="Fields cannot be empty.")
    if len(password) < 6:
        return render_template("index.html", error="Password must be at least 6 characters.")

    return render_template("index.html", message=f"Welcome, {username}!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)