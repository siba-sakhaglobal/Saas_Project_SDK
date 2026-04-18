"""Team module models."""

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class TeamMember(BaseModel):
    """Team member."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    project_id: Optional[str] = Field(None, alias="project_id")
    name: str
    email: str
    phone: Optional[str] = None
    role: str  # admin|editor|viewer
    avatar_url: Optional[str] = Field(None, alias="avatar_url")
    is_active: bool = Field(default=True, alias="is_active")
    joined_at: datetime = Field(alias="joined_at")
    created_at: datetime = Field(alias="created_at")
    updated_at: datetime = Field(alias="updated_at")


class CreateTeamMemberBody(BaseModel):
    """Create team member request."""

    model_config = ConfigDict(populate_by_name=True)

    name: str
    email: str
    phone: Optional[str] = None
    role: str = "viewer"
    avatar_url: Optional[str] = Field(None, alias="avatarUrl")


class UpdateTeamMemberBody(BaseModel):
    """Update team member request."""

    model_config = ConfigDict(populate_by_name=True)

    name: Optional[str] = None
    phone: Optional[str] = None
    role: Optional[str] = None
    avatar_url: Optional[str] = Field(None, alias="avatarUrl")
    is_active: Optional[bool] = Field(None, alias="isActive")


class TeamStats(BaseModel):
    """Team statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total_members: int = Field(alias="totalMembers")
    active_members: int = Field(alias="activeMembers")
    admin_members: int = Field(alias="adminMembers")
    editor_members: int = Field(alias="editorMembers")
    viewer_members: int = Field(alias="viewerMembers")
