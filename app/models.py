'''
This module deines data models for the application using SQLModel as the ORM.
These models define the structure of the database tables and the data validation for incoming requests.

'''

from sqlmodel import SQLModel, Field
from typing import Optional


# A class representing a user in the database.
# It inherits from SQLModel and defines the fields for the user table.
class User(SQLModel, table=True):
    __tablename__ = "users"  # 👈 Force table name to be "users"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str
    role: str  # 'admin' or 'user'


# A class representing a user creation request.
# It inherits from SQLModel and defines the fields for creating a new user.
class UserCreate(SQLModel):
    username: str
    password: str
    role: str


# A class representing a user login request.
# It inherits from SQLModel and defines the fields for user login.
class UserLogin(SQLModel):
    username: str
    password: str


# A class representing a JWT token response.
# It inherits from SQLModel and defines the fields for the token response.
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# A class representing a project in the database.
# It inherits from SQLModel and defines the fields for the project table.
class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str


# A class representing a project creation request.
# It inherits from SQLModel and defines the fields for creating a new project.
class ProjectCreate(SQLModel):
    name: str
    description: str
