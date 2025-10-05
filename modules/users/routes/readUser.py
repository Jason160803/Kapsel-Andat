from fastapi import APIRouter, HTTPException, status
from typing import List
from modules.users.schema.schemas import UserResponse, ResponseModel

router = APIRouter()
users: List[UserResponse] = []

@router.get("/users/", response_model=ResponseModel, status_code=status.HTTP_200_OK)
def read_users():
    """
    Mengembalikan semua user yang ada.
    """
    return ResponseModel(
        success=True,
        message=f"Total {len(users)} user(s) found",
        data=users
    )

@router.get("/users/{user_id}", response_model=ResponseModel, status_code=status.HTTP_200_OK)
def read_user(user_id: str):
    """
    Mengembalikan data user berdasarkan user_id.
    """
    for user in users:
        if user.id == user_id:
            return ResponseModel(
                success=True,
                message="User found",
                data=user
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )