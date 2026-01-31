import secrets
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.config.settings import settings

security = HTTPBasic()


def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    """Verify admin credentials using HTTP Basic Auth"""
    correct_username = secrets.compare_digest(
        credentials.username.encode("utf8"), settings.admin_username.encode("utf8")
    )
    correct_password = secrets.compare_digest(
        credentials.password.encode("utf8"), settings.admin_password.encode("utf8")
    )

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username
