"""Users module models."""

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class User(BaseModel):
    """User."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: str
    name: Optional[str] = None
    avatar_url: Optional[str] = Field(None, alias="avatar_url")
    role: str = "user"  # user|admin|moderator
    is_active: bool = Field(default=True, alias="is_active")
    email_verified: bool = Field(default=False, alias="email_verified")
    last_login: Optional[datetime] = Field(None, alias="last_login")
    created_at: datetime = Field(alias="created_at")
    updated_at: datetime = Field(alias="updated_at")


class CreateUserBody(BaseModel):
    """Create user request."""

    model_config = ConfigDict(populate_by_name=True)

    email: str
    name: Optional[str] = None
    password: str
    avatar_url: Optional[str] = Field(None, alias="avatarUrl")
    role: str = "user"


class UpdateUserBody(BaseModel):
    """Update user request."""

    model_config = ConfigDict(populate_by_name=True)

    name: Optional[str] = None
    avatar_url: Optional[str] = Field(None, alias="avatarUrl")
    role: Optional[str] = None
    is_active: Optional[bool] = Field(None, alias="isActive")
    password: Optional[str] = None


class UserStats(BaseModel):
    """User statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total_users: int = Field(alias="totalUsers")
    active_users: int = Field(alias="activeUsers")
    admin_users: int = Field(alias="adminUsers")
    moderator_users: int = Field(alias="moderatorUsers")
    email_verified_users: int = Field(alias="emailVerifiedUsers")
