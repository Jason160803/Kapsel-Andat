from fastapi import APIRouter, HTTPException, status
from typing import List
from modules.users.schema.schemas import UserCreate, UserResponse, ResponseModel
from datetime import datetime, timezone
import uuid

router = APIRouter()
users: List[UserResponse] = []


@router.post("/users/", response_model=ResponseModel, status_code=201)
def create_user(user: UserCreate):
    """
    Create a new user.
    Accessible by anyone.
    """

    if any(u.username == user.username for u in users):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    if any(u.email == user.email for u in users):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    new_user = UserResponse(
        id=str(uuid.uuid4()),
        username=user.username,
        email=user.email,
        role=user.role,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc)
    )

    users.append(new_user)

    return ResponseModel(
        success=True,
        message="New user successfully created",
        data=new_user
    )