"""Media module models."""

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class Media(BaseModel):
    """Media file."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    project_id: Optional[str] = Field(None, alias="project_id")
    filename: str
    original_name: Optional[str] = Field(None, alias="original_name")
    mime_type: str = Field(alias="mime_type")
    size_bytes: int = Field(alias="size_bytes")
    url: str
    folder: Optional[str] = None
    description: Optional[str] = None
    alt_text: Optional[str] = Field(None, alias="alt_text")
    tags: list[str] = Field(default_factory=list)
    created_at: datetime = Field(alias="created_at")
    updated_at: datetime = Field(alias="updated_at")


class CreateMediaBody(BaseModel):
    """Create media request."""

    model_config = ConfigDict(populate_by_name=True)

    filename: str
    original_name: Optional[str] = Field(None, alias="originalName")
    mime_type: str = Field(alias="mimeType")
    size_bytes: int = Field(alias="sizeBytes")
    url: str
    folder: Optional[str] = None
    description: Optional[str] = None
    alt_text: Optional[str] = Field(None, alias="altText")
    tags: Optional[list[str]] = None


class UpdateMediaBody(BaseModel):
    """Update media request."""

    model_config = ConfigDict(populate_by_name=True)

    original_name: Optional[str] = Field(None, alias="originalName")
    description: Optional[str] = None
    alt_text: Optional[str] = Field(None, alias="altText")
    folder: Optional[str] = None
    tags: Optional[list[str]] = None


class MediaStats(BaseModel):
    """Media statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total_files: int = Field(alias="totalFiles")
    total_size_mb: float = Field(alias="totalSizeMb")
    total_images: int = Field(alias="totalImages")
    total_videos: int = Field(alias="totalVideos")
    total_documents: int = Field(alias="totalDocuments")
    total_other: int = Field(alias="totalOther")
