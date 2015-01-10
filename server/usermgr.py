import os, hashlib

# Attempt to authenticate a user, returning an access token
def login(username, password):
    # Look up the user in the database

    # Hash the password (along with the salt)
    sha512 = hashlib.sha512()
    sha512.update(bytes(password))
    password_hash = sha512.digest()

    # Verify the user's hash
