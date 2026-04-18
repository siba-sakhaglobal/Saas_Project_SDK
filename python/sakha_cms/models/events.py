"""Events module models."""

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class EventCategory(BaseModel):
    """Event category."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    name: str
    color: str = "#64748B"
    sort_order: int = Field(default=0, alias="sortOrder")


class Event(BaseModel):
    """Event."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    slug: str
    description: Optional[str] = None
    content: Optional[str] = None  # alias for description
    location: Optional[str] = None
    venue: Optional[str] = None  # alias for location
    event_date: datetime = Field(alias="event_date")
    event_time: str = Field(default="", alias="event_time")
    end_date: Optional[datetime] = Field(None, alias="end_date")
    end_time: Optional[str] = Field(None, alias="end_time")
    image: Optional[str] = None
    image_url: Optional[str] = Field(None, alias="image_url")
    featured_image: Optional[str] = Field(None, alias="featured_image")
    category: Optional[EventCategory] = None
    status: str  # upcoming|ongoing|completed|cancelled
    is_featured: bool = Field(default=False, alias="is_featured")
    max_participants: Optional[int] = Field(None, alias="max_participants")
    registration_count: int = Field(default=0, alias="registration_count")
    registration_fee: int = Field(default=0, alias="registration_fee")
    contact_person: Optional[str] = Field(None, alias="contact_person")
    contact_email: Optional[str] = Field(None, alias="contact_email")
    contact_phone: Optional[str] = Field(None, alias="contact_phone")
    visibility: str = "public"
    tags: list[str] = Field(default_factory=list)
    created_at: datetime = Field(alias="created_at")
    updated_at: datetime = Field(alias="updated_at")


class CreateEventBody(BaseModel):
    """Create event request."""

    model_config = ConfigDict(populate_by_name=True)

    project_id: Optional[str] = Field(None, alias="projectId")
    title: str
    slug: Optional[str] = None
    description: str
    content: Optional[str] = None
    location: str
    venue: Optional[str] = None
    event_date: datetime = Field(alias="event_date")
    event_time: Optional[str] = Field(None, alias="event_time")
    end_date: Optional[datetime] = Field(None, alias="end_date")
    end_time: Optional[str] = Field(None, alias="end_time")
    image_id: Optional[str] = Field(None, alias="image_id")
    category: Optional[str] = None
    status: str = "upcoming"
    max_participants: Optional[int] = Field(None, alias="max_participants")
    registration_fee: Optional[float] = Field(None, alias="registration_fee")
    contact_person: Optional[str] = Field(None, alias="contact_person")
    contact_email: Optional[str] = Field(None, alias="contact_email")
    contact_phone: Optional[str] = Field(None, alias="contact_phone")
    is_featured: bool = Field(default=False, alias="is_featured")
    tags: Optional[list[str]] = None


class UpdateEventBody(BaseModel):
    """Update event request."""

    model_config = ConfigDict(populate_by_name=True)

    title: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None
    location: Optional[str] = None
    venue: Optional[str] = None
    event_date: Optional[datetime] = Field(None, alias="event_date")
    event_time: Optional[str] = Field(None, alias="event_time")
    end_date: Optional[datetime] = Field(None, alias="end_date")
    end_time: Optional[str] = Field(None, alias="end_time")
    image_id: Optional[str] = Field(None, alias="image_id")
    category: Optional[str] = None
    status: Optional[str] = None
    max_participants: Optional[int] = Field(None, alias="max_participants")
    registration_fee: Optional[float] = Field(None, alias="registration_fee")
    contact_person: Optional[str] = Field(None, alias="contact_person")
    contact_email: Optional[str] = Field(None, alias="contact_email")
    contact_phone: Optional[str] = Field(None, alias="contact_phone")
    is_featured: Optional[bool] = Field(None, alias="is_featured")
    tags: Optional[list[str]] = None


class CreateEventCategoryBody(BaseModel):
    """Create event category request."""

    model_config = ConfigDict(populate_by_name=True)

    name: str
    color: str = "#64748B"
    sort_order: int = Field(default=0, alias="sortOrder")


class UpdateEventCategoryBody(BaseModel):
    """Update event category request."""

    model_config = ConfigDict(populate_by_name=True)

    name: Optional[str] = None
    color: Optional[str] = None
    sort_order: Optional[int] = Field(None, alias="sortOrder")


class EventStats(BaseModel):
    """Event statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total: int
    upcoming: int
    ongoing: int
    completed: int
    cancelled: int
    total_registrations: int = Field(alias="totalRegistrations")
