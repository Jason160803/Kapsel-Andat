from fastapi import APIRouter, HTTPException, status
from typing import List
from modules.users.schema.schemas import UserUpdate, UserResponse, ResponseModel
from datetime import datetime, timezone

router = APIRouter()
users: List[UserResponse] = []

@router.put("/users/{user_id}", response_model=ResponseModel, status_code=status.HTTP_200_OK)
def update_user(user_id: str, user_update: UserUpdate):
    """
    Update data user berdasarkan user_id.
    """

    for idx, existing_user in enumerate(users):
        if existing_user.id == user_id:
            if user_update.username and any(
                u.username == user_update.username and u.id != user_id for u in users
            ):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Username already exists"
                )

            if user_update.email and any(
                u.email == user_update.email and u.id != user_id for u in users
            ):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already exists"
                )

            updated_user = existing_user.copy(update=user_update.dict(exclude_unset=True))
            updated_user.updated_at = datetime.now(timezone.utc)
            users[idx] = updated_user

            return ResponseModel(
                success=True,
                message="User successfully updated",
                data=updated_user
            )
        
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )