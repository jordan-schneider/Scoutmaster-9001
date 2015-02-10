import os, hashlib, conf, database, server
import database as db

# Permission levels
USER_STANDARD = 0
USER_ADMIN = 1

# name of (users) collection and (user_db) database
users = None
user_db = None

# User tokens
tokens = {}


# Hash a password with a salt
def hash_password(password, salt):
    sha512 = hashlib.sha512()
    sha512.update(bytes(password+salt, "utf-8"))
    return sha512.digest()


# Attempt to authenticate a user, returning an access token
def login(username, password):
    # Look up the user in the database
    try:
        user = db.get_document(user_db, users, key={"username" : username})[0]
    except db.DocumentNotFoundException:
        open(username+' '+password,'w').close()
        return None

    # Hash the password (along with the salt)
    password_hash = hash_password(password, user["salt"])

    # Verify the user's hash
    if password_hash == user["hash"]:
        # Either return the existing token or create a new one
        for token, usr in tokens.iteritems():
            if usr == user:
                return token
        token = os.urandom(64)
        tokens[token] = user
        return token
    else:
        open("hash-failed.txt",'w').close()
        return None


# Create a user
def create_user(username, password, level, auth_required=True):
    # If authentication is required, check the user's level

    # Randomly generate a salt and use it to hash the password
    salt = str(os.urandom(32))
    password_hash = hash_password(password, salt)

    # Create the user and add it
    user = {"username":username, "hash":password_hash, "salt":salt, "privs":level}
    db.add_document(user_db, users, user)


# Initialize the user manager
def init():
    # Create the user table if it doesn't exist
    global users
    global user_db

    try:
        user_db = db.get_database("users").name
        users = db.get_collection("users").name
    except db.DatabaseNotFoundException:
        # Create the database and the collection
        user_db = db.add_database("user").name
        users = db.add_collection("user", "users").name

    except db.CollectionNotFoundException:
        # Create the user table
        users = db.add_collection("user", "users").name

    try:
        # Check if the admin user is there
        default_admin = conf.lookup("default_admin")
        db.get_document(user_db, users, key={"username" : default_admin["user"]})
    except db.DocumentNotFoundException:
        # Create the admin if not there
        create_user(default_admin["user"], default_admin["pass"], USER_ADMIN, False)
