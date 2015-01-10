from flask import Flask, session, redirect, url_for, escape, request

import usermgr

app = Flask(__name__)

# Root URL
@app.route("/")
def index():
    # Already logged in
    if "token" in session:
        return redirect(url_for("teams"))
    # Not logged in
    else:
        return redirect(url_for("login"))

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    # Sending credentials
    if request.method == "POST":
        # Get the username and password from the webform
        username = request.form["username"]
        password = request.form["password"]

        # Attempt to login
        token = usermgr.login(username, password)

        # Give them access if the password check succeeded
        if token:
            session["token"] = token
            return redirect(url_for("index"))

    # GET request or authentication failure
    return open("login.html").read()

# Logout page
@app.route("/logout")
def logout():
    session.pop("token", None)
    return redirect(url_for("index"))

# Initialize the server
def server_init():
    app.run(port=9001)
