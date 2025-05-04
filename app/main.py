'''
Simple API with JWT Authentication and Role-Based Access Control (RBAC).
This is a simple API that demonstrates how to implement JWT authentication and role-based access control (RBAC) using SQLModel as the ORM.
'''


from fastapi import FastAPI
from app.routes import router
from app.database import init_db


# Initialize the FastAPI application and include the router for API routes
# The router contains all the endpoints for user registration, login, and project management.
app = FastAPI(
    title="Simple API",
    description=""" 
    A RESTful API that implements user authentication with JWT (JSON Web Token) and \
Role-Based Access Control (RBAC). The API manages users with different roles and \
restricts access to certain endpoints based on the user’s role.
 
    Features:  
    - User authentication (JWT)
    - Role-based access control (RBAC)
    - User registration/login
    - Create/read projects  
    - Sort projects by ID (asc/desc) when getting all projects
    - Admin-only project creation, updation and deletion 
    """,
    version="1.0.0",
)


# Include the router in the FastAPI application
# This allows the application to handle requests to the defined endpoints in the router.
app.include_router(router)


# Initialize the database when the application starts
# Call the init_db function to create the database tables defined in the SQLModel models.
@app.on_event("startup")
def on_startup():
    init_db()


# Define a root endpoint that returns a welcome message
# This endpoint can be used to check if the API is running and accessible.
@app.get("/", include_in_schema=False)
def read_root():
    return {"message": "Welcome to Simple API with JWT Authentication and RBAC!"}
