from fastapi import APIRouter, HTTPException, status
from typing import List
from modules.users.schema.schemas import UserResponse, ResponseModel

router = APIRouter()
users: List[UserResponse] = []

@router.delete("/users/{user_id}", response_model=ResponseModel, status_code=status.HTTP_200_OK)
def delete_user(user_id: str):
    """
    Delete a user by user_id.
    """
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return ResponseModel(
                success=True,
                message=f"User with id {user_id} deleted successfully",
                data=deleted_user
            )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )