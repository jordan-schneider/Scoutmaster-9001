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


# Initialize the user manager
def init():
    # Create the user table if it doesn't exist
    global users
    try:
        users = database.get_collection("users")
    except:
        # Create the user table
        users = database.add_collection("users")

    # Add the admin user if it's not in there
    default_admin = conf.lookup("default_admin")
    if users.find_one({"username" : default_admin["user"]}) == None: #EDIT
        # Get the default admin credentials and create it as a user
        create_user(default_admin["user"], default_admin["pass"], USER_ADMIN, False)
