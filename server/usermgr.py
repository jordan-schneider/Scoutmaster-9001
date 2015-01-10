import os, hashlib
import conf, database

# Permission levels
USER_STANDARD = 0
USER_ADMIN = 1

# User table in the database
users = None

# User tokens
tokens = {}

# Attempt to authenticate a user, returning an access token
def login(username, password):
    # Look up the user in the database
    user = users.find_one(username=username)
    if user == None:
        return None

    # Hash the password (along with the salt)
    sha512 = hashlib.sha512()
    sha512.update(bytes(password+user["salt"]))
    password_hash = sha512.digest()

    # Verify the user's hash
    if password_hash == user["hash"]:
        # Get a user-to-token dict
        reverse_tokens = {v:k for k,v in tokens.items()}

        # Either return the existing token or create a new one
        try:
            token = reverse_tokens[user]
            return token
        except KeyError:
            token = os.urandom(64)
            tokens[token] = user
            return token
    else:
        return None

# Create a user
def create_user(username, password, level):
    pass

# Initialize the user manager
def init():
    # Create the user table if it doesn't exist
    users = database.get_table("users")
    if users == None:
        # Create the user table
        users = database.add_table("users")
        
        # Get the default admin credentials and create it as a user
        default_admin = conf.lookup("default_admin")
        create_user(default_admin["user"], default_admin["pass"], USER_ADMIN)
