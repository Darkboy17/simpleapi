'''
    JWT Authentication and Password Hashing
    This module provides functions for creating and verifying JWT tokens,
'''


from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
import os
from dotenv import load_dotenv


# Load environment variables from .env file
# This is important for keeping sensitive information like secret keys and database URLs out of the codebase.
load_dotenv()


# Environment variables for JWT authentication
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


# Password hashing context
# This context is used to hash passwords securely using the bcrypt algorithm.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# A function to hash a password using the bcrypt algorithm.
# This function takes a plain password as input and returns the hashed password.
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# A function to verify a plain password against a hashed password.
# This function takes a plain password and a hashed password as input and returns True if they match, False otherwise.
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# A function to create a JWT access token.
# This function takes a dictionary of data as input, adds an expiration time to it, and encodes it using the secret key and algorithm.
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# A function to decode a JWT token and retrieve the payload.
# This function takes a token as input and decodes it using the secret key and algorithm.
def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
