from typing import Optional, List, Union
from pydantic import BaseModel, Field, EmailStr, ConfigDict, field_validator
from enum import Enum
from datetime import datetime
import re


class UserRole(str, Enum):
    admin = "admin"
    staff = "staff"


class UserBase(BaseModel):
    username: str = Field(
        ...,
        min_length=6,
        max_length=15,
        pattern=r"^[a-z0-9]+$",
        title="username",
        description="must be lowercase alphanumeric (between 6–15 characters)",
        example="johndoe777"
    )
    email: EmailStr = Field(..., example="johndoe777@gmail.com")
    role: UserRole = Field(..., example="staff")

class UserCreate(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=20,
        description="Password must include uppercase, lowercase, digit, and special character (! or @)",
        example="Johndoe777@"
    )

    @field_validator("password")
    def validate_password(cls, v: str):
        if not re.fullmatch(r"[A-Za-z0-9!@]{8,20}", v):
            raise ValueError("Password contains invalid characters or wrong length")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[!@]", v):
            raise ValueError("Password must contain at least one special character (! or @)")
        return v

    model_config = ConfigDict(extra="forbid")

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=6, max_length=15, pattern=r"^[a-z0-9]+$")
    email: Optional[EmailStr] = None
    role: Optional[UserRole] = None
    password: Optional[str] = None

    @field_validator("password")
    def validate_password(cls, v: Optional[str]):
        if v is None:
            return v
        if not re.fullmatch(r"[A-Za-z0-9!@]{8,20}", v):
            raise ValueError("Password contains invalid characters or wrong length")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[!@]", v):
            raise ValueError("Password must contain at least one special character (! or @)")
        return v

    model_config = ConfigDict(extra="forbid")

class UserResponse(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime

class ResponseModel(BaseModel):
    success: bool
    message: str
    data: Optional[Union[UserResponse, List[UserResponse]]] = None