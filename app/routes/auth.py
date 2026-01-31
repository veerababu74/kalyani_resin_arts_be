from fastapi import APIRouter, Depends
from app.auth.basic_auth import verify_credentials

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login")
async def login(username: str = Depends(verify_credentials)):
    """Login endpoint - verifies credentials"""
    return {"message": "Login successful", "username": username}


@router.get("/verify")
async def verify_token(username: str = Depends(verify_credentials)):
    """Verify if the token/credentials are still valid"""
    return {"valid": True, "username": username}
