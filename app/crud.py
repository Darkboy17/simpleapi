'''
A module for CRUD operations on the database models.
'''


from fastapi import HTTPException
from sqlmodel import Session, select
from app.models import User, Project, UserCreate, ProjectCreate
from app.auth import hash_password, verify_password


# A function to create a new user in the database.
# It takes a session and user data as input, hashes the password, and adds the user to the session.
def create_user(session: Session, user_data: UserCreate):
    existing_user = session.exec(select(User).where(
        User.username == user_data.username)).first()
    if existing_user:
        raise HTTPException(
            status_code=400, detail="Username already registered")

    if user_data.role not in ["admin", "user"]:
        raise HTTPException(
            status_code=400, detail="Invalid role. Use 'admin' or 'user'.")

    user = User(
        username=user_data.username,
        hashed_password=hash_password(user_data.password),
        role=user_data.role
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


# A function to authenticate a user by checking the username and password.
# It retrieves the user from the database and verifies the password.
def authenticate_user(session: Session, username: str, password: str):
    user = session.exec(select(User).where(User.username == username)).first()
    if user and verify_password(password, user.hashed_password):
        return user
    return None


# A function to retrieve a user by username.
# It uses a SQLAlchemy query to select the user from the database.
def get_user_by_username(session: Session, userid: str):
    # returns the first user that matches the username
    return session.exec(select(User).where(User.id == userid)).first()

# A function to get the next available project ID.
# It retrieves all used IDs from the database and finds the smallest missing positive integer.
def get_next_available_project_id(session: Session) -> int:
    # Get all used IDs, ordered
    used_ids = session.exec(select(Project.id).order_by(Project.id)).all()

    # Find the smallest missing positive integer
    current = 1
    for used_id in used_ids:
        if used_id != current:
            return current
        current += 1
    return current  # If no gaps, return next highest


# A function to create a new project in the database.
# It takes a session and project data as input, creates a new Project object, and adds it to the session.
def create_project(session: Session, project: ProjectCreate):

    # Check if project with the same name already exists
    existing_project = session.exec(
        select(Project).where(Project.name == project.name)
    ).first()

    if existing_project:
        raise HTTPException(
            status_code=400, detail="Project with this name already exists")

    new_id = get_next_available_project_id(session)
    db_project = Project(id=new_id, **project.dict())
    session.add(db_project)
    session.commit()
    session.refresh(db_project)
    return db_project


# A function to retrieve all projects from the database.
# It uses a SQLAlchemy query to select all projects from the Project table.
def get_projects(session: Session, sort_by: str = "desc"):
    if sort_by not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400, detail="Invalid sort parameter. Use 'asc' or 'desc'.")

    order = Project.id.asc() if sort_by == "asc" else Project.id.desc()
    return session.exec(select(Project).order_by(order)).all()
