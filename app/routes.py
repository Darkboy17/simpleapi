'''
This module defines the API routes for user registration, login, and project management.
It uses FastAPI to create the endpoints and SQLModel for database interactions.
'''


from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.models import UserCreate, UserLogin, Token, ProjectCreate, Project
from app.auth import create_access_token
from app.crud import create_user, authenticate_user, create_project, get_projects
from app.dependencies import get_current_user, require_admin
from app.database import get_session


# This router will be included in the main FastAPI app
router = APIRouter()


# A route or endpoint to register a new user
@router.post("/register", summary="Register a new user",
             description="""  
    Creates a new user in the system.  
    - Requires a valid `username`, `password`, and `role`.  
    - Returns the created user details.  
    """)
def register(user_data: UserCreate, session: Session = Depends(get_session)):
    return create_user(session, user_data)


# A route or endpoint to login a user and return a JWT token
# This route uses the UserLogin model to validate the credentials and returns a Token model with the access token
@router.post("/login", response_model=Token, summary="User login",
             description="""  
    Authenticates a user and returns a JWT token.  
    - Requires a valid `username` and `password`.  
    - Returns an access token for authentication.  
    """)
def login(credentials: UserLogin, session: Session = Depends(get_session)):
    user = authenticate_user(
        session, credentials.username, credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(data={"sub": str(user.id), "role": user.role})
    return {"access_token": token}


# A route or endpoint to get all projects
# This route uses the get_projects function to retrieve all projects from the database
@router.get("/projects", summary="List all projects",
            description="""  
    Returns a list of all projects. Both admin and user roles can access this endpoint.  
    - **sort_by**: Sort order (`asc` or `desc`).  
    - Requires authentication.  
    """,
            )
def read_projects(session: Session = Depends(get_session), user=Depends(get_current_user), sort_by: str = "desc"):
    return get_projects(session, sort_by=sort_by)


# A route or endpoint to create a new project
# This route uses the ProjectCreate model to validate the project data and returns the created project
@router.post("/projects", summary="Create a new project",
             description="""  
    Creates a new project in the system.  
    - Requires a valid `name` and `description`.  
    - Returns the created project details.  
    """)
def add_project(project: ProjectCreate, session: Session = Depends(get_session), user=Depends(require_admin)):
    return {"detail": "Project created successfully", "project": create_project(session, project)}


# A route or endpoint to get a specific project by its ID and delete it
# This route uses the Project model to validate the project data and returns the deleted project with a success message
@router.delete("/projects/{project_id}", summary="Delete a project",
               description="""  
    Deletes a specific project by its ID.  
    - Requires a valid `project_id`.  
    - Requires admin authentication.  
    - Returns a success message with the deleted project details.  
    """)
def delete_project(
    project_id: int,
    session: Session = Depends(get_session),
    user=Depends(require_admin)
):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    session.delete(project)
    session.commit()
    return {"detail": "Project deleted successfully", "project": project}


# A route or endpoint to update a specific project by its ID
# This route uses the ProjectCreate model to validate the updated project data and returns the updated project with a success message
@router.put("/projects/{project_id}", summary="Update a project",
            description="""  
    Updates a specific project by its ID.  
    - Requires a valid `project_id`.  
    - Requires admin authentication.  
    - Returns a success message with the updated project details.  
    """)
def update_project(
    project_id: int,
    updated: ProjectCreate,
    session: Session = Depends(get_session),
    user=Depends(require_admin)
):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if updated.name != "string" and updated.name != project.name:
        project.name = updated.name
    if updated.description != "string" and updated.description != project.description:
        project.description = updated.description

    if updated.name == "string" and updated.description == "string":
        return {"detail": "You have not made any changes to update the project details", "project": project}

    session.add(project)
    session.commit()
    session.refresh(project)
    return {"detail": "Project updated successfully", "project": project}
