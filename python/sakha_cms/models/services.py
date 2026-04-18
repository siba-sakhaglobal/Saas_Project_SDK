"""Services module models."""

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class Service(BaseModel):
    """Service."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    project_id: Optional[str] = Field(None, alias="project_id")
    name: str
    slug: str
    description: Optional[str] = None
    image_url: Optional[str] = Field(None, alias="image_url")
    price: float
    duration_minutes: Optional[int] = Field(None, alias="duration_minutes")
    category: Optional[str] = None
    is_active: bool = Field(default=True, alias="is_active")
    is_featured: bool = Field(default=False, alias="is_featured")
    sort_order: int = Field(default=0, alias="sort_order")
    created_at: datetime = Field(alias="created_at")
    updated_at: datetime = Field(alias="updated_at")


class CreateServiceBody(BaseModel):
    """Create service request."""

    model_config = ConfigDict(populate_by_name=True)

    name: str
    slug: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = Field(None, alias="imageUrl")
    price: float
    duration_minutes: Optional[int] = Field(None, alias="durationMinutes")
    category: Optional[str] = None
    is_active: bool = Field(default=True, alias="isActive")
    is_featured: bool = Field(default=False, alias="isFeatured")
    sort_order: int = Field(default=0, alias="sortOrder")


class UpdateServiceBody(BaseModel):
    """Update service request."""

    model_config = ConfigDict(populate_by_name=True)

    name: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = Field(None, alias="imageUrl")
    price: Optional[float] = None
    duration_minutes: Optional[int] = Field(None, alias="durationMinutes")
    category: Optional[str] = None
    is_active: Optional[bool] = Field(None, alias="isActive")
    is_featured: Optional[bool] = Field(None, alias="isFeatured")
    sort_order: Optional[int] = Field(None, alias="sortOrder")


class ServiceStats(BaseModel):
    """Service statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total_services: int = Field(alias="totalServices")
    active_services: int = Field(alias="activeServices")
    featured_services: int = Field(alias="featuredServices")
    total_revenue: float = Field(alias="totalRevenue")
    average_price: float = Field(alias="averagePrice")
