import os, hashlib
import database

# User tokens
tokens = {}

# Attempt to authenticate a user, returning an access token
def login(username, password):
    # Look up the user in the database
    users = database.db_get_table("users")
    user = users.find_one(username=username)
    if not user:
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
