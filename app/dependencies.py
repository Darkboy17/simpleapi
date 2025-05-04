'''
Dependencies for FastAPI routes. This module contains functions that are used to extract and validate data from requests, such as authentication tokens and user information.
It also includes functions to enforce role-based access control (RBAC) by checking user roles before allowing access to certain routes.
'''


from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from app.auth import decode_token
from app.database import get_session
from sqlmodel import Session
from app.crud import get_user_by_username


# This module provides dependencies for FastAPI routes, including authentication and authorization checks.
# It uses JWT tokens for authentication and checks user roles for access control.
oauth2_scheme = APIKeyHeader(name="Authorization")


# This function decodes the JWT token and retrieves the user information.
# It raises an HTTPException if the token is invalid or if the user is not found.
def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    payload = decode_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    user = get_user_by_username(session, payload.get("sub"))
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# This function checks if the user has admin privileges.
# It raises an HTTPException if the user does not have the required role.
def require_admin(user=Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(
            status_code=403, detail="You don't have permission to perform this action. Please contact your administrator.")
    return user
