from flask import Flask, session, redirect, url_for, request, render_template

import conf, user_handler

app = Flask(__name__)

# Handler statuses
HTTP_OK = 200
HTTP_NOT_FOUND = 404

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
        token = user_handler.login(username, password)

        # Give them access if the password check succeeded
        if token:
            session["token"] = token
            return redirect(url_for("index"))
        else:
            return redirect(url_for("login", login_failed=True))

    # GET request or authentication failure
    login_failed = False
    if "login_failed" in request.args:
        login_failed = True
    return render_template("login.html", login_failed=login_failed)

# Specific user page
@app.route("/user/<int:uid>")
def user_page(uid):
    # Getting user information
    if request.method == "GET":
        pass
    # Changing user information
    elif request.method == "POST":
        status = edit_user(uid, 

# Logout page
@app.route("/logout")
def logout():
    session.pop("token", None)
    return redirect(url_for("index"))

# Initialize the server
def init():
    app.secret_key = conf.lookup("secret_key")
    app.run(port=9001, debug=True)
