import os, hashlib
import conf, database, server

# Permission levels
USER_STANDARD = 0
USER_ADMIN = 1

# User table in the database
users = None

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
    user = users.find_one(username=username)
    if user == None:
        return None

    # Hash the password (along with the salt)
    password_hash = hash_password(password, user["salt"])

    # Verify the user's hash
    if password_hash == user["hash"]:
        # Either return the existing token or create a new one
        if user in tokens.values():
            token = reverse_tokens[user]
            return token
        else:
            token = os.urandom(64)
            tokens[token] = user
            return token
    else:
        return None


# Create a user
def create_user(username, password, level, auth_required=True):
    # If authentication is required, check the user's level

    # Randomly generate a salt and use it to hash the password
    salt = str(os.urandom(32))
    password_hash = hash_password(password, salt)

    # Create the user and add it
    user = {"username":username, "hash":password_hash, "salt":salt, "privs":level}
    users.insert(user)


# Get a user's information
def get_user(uid):
    # Look up the user in the database
    rows = users.all()
    user = rows.next()
    while uid > 0 and user != None:
        user = rows.next()
        uid -= 1

    # Return it
    if user == None:
        return server.HTTP_NOT_FOUND
    return user


# Edit a user's information
def edit_user(uid, new_password, new_level, auth_required=True):
    # Look up the user in the database
    rows = users.all()
    user = rows.next()
    while uid > 0 and user != None:
        user = rows.next()
        uid -= 1

    # If the user isn't found, fail the request
    if user == None:
        return server.HTTP_NOT_FOUND

    # If authentication is required, check the user's level

    # Change the password if desired
    if password != None:
        user["hash"] = hash_password(new_password, user["salt"])

    # Change the authentication level if desired
    if new_level != None:
        user["level"] = new_level


# Initialize the user manager
def init():
    # Create the user table if it doesn't exist
    global users
    try:
        users = database.get_table("users")
    except:
        # Create the user table
        users = database.add_table("users")

    # Add the admin user if it's not in there
    if "username" not in users.columns:
        # Get the default admin credentials and create it as a user
        default_admin = conf.lookup("default_admin")
        create_user(default_admin["user"], default_admin["pass"], USER_ADMIN, False)
