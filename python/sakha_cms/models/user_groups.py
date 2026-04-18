"""User Groups module models."""

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class UserGroup(BaseModel):
    """User group."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    project_id: Optional[str] = Field(None, alias="project_id")
    name: str
    slug: str
    description: Optional[str] = None
    member_count: int = Field(default=0, alias="member_count")
    is_active: bool = Field(default=True, alias="is_active")
    permissions: list[str] = Field(default_factory=list)
    created_at: datetime = Field(alias="created_at")
    updated_at: datetime = Field(alias="updated_at")


class CreateUserGroupBody(BaseModel):
    """Create user group request."""

    model_config = ConfigDict(populate_by_name=True)

    name: str
    slug: Optional[str] = None
    description: Optional[str] = None
    permissions: Optional[list[str]] = None


class UpdateUserGroupBody(BaseModel):
    """Update user group request."""

    model_config = ConfigDict(populate_by_name=True)

    name: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = Field(None, alias="isActive")
    permissions: Optional[list[str]] = None


class UserGroupStats(BaseModel):
    """User group statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total_groups: int = Field(alias="totalGroups")
    active_groups: int = Field(alias="activeGroups")
    total_members: int = Field(alias="totalMembers")
    average_group_size: float = Field(alias="averageGroupSize")
