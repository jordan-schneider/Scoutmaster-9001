from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

# Root URL
@app.route("/")
def index():
    # Already logged in
    if "username" in session:
        return redirect(url_for("teams"))
    # Not logged in
    else:
        return redirect(url_for("login"))

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    # Sending credentials
    if request.method == "POST":
        pass
    # Getting the login page
    elif request.method == "GET":
        pass

# Logout page
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

