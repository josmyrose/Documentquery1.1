from fastapi import APIRouter, HTTPException
from app.schemas import UserCreate, UserLogin, TokenResponse
from app.services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
def register(payload: UserCreate):
    try:
        return register_user(payload.email, payload.password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=TokenResponse)
def login(payload: UserLogin):
    try:
        return login_user(payload.email, payload.password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))