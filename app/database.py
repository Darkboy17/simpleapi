'''
Database connection and session management for SQLModel.
'''


from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


# Database URL from environment variable
# This URL contains the database type, username, password, host, port, and database name.
DATABASE_URL = os.getenv("ORACLE_POSTGRES_URL")


# Create a SQLModel engine using the database URL
# The engine is responsible for managing the connection to the database and executing SQL queries.
try:
    engine = create_engine(DATABASE_URL, echo=True)
except Exception as e:
    raise RuntimeError(f"Failed to create database engine: {e}")

# Function to get the engine
# This function returns the engine object created above to be used for generating project mock-data.


def get_engine():
    return engine

# Create a session generator function
# This function creates a new session for each request and closes it after use.


def get_session():
    with Session(engine) as session:
        yield session


# Function to initialize the database
# This function creates all the tables defined in the SQLModel models.
def init_db():
    SQLModel.metadata.create_all(engine)
