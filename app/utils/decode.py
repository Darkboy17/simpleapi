''''
For debugging purposes only,

This module provides functions for decoding JWT tokens and extracting the payload data.
It can be used to decode a JWT token and print the payload data.
'''

from jose import jwt
from dotenv import load_dotenv
import os

# Load environment variables from .env file
# This is necessary to access the SECRET_KEY used for signing the JWT tokens.
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")


# Input your JWT token here to check the payload
# This is a placeholder for the JWT token you want to decode.
token = ""

# Decode the JWT token using the secret key and the HS256 algorithm
# The decode function verifies the token and extracts the payload data.
payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

# Print the decoded payload data
# This will display the contents of the JWT token, including the user ID and role.
print(payload)
