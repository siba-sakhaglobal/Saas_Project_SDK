"""Vendors module models."""

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class Vendor(BaseModel):
    """Vendor."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    project_id: Optional[str] = Field(None, alias="project_id")
    name: str
    slug: str
    description: Optional[str] = None
    email: str
    phone: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    zip_code: Optional[str] = Field(None, alias="zip_code")
    logo_url: Optional[str] = Field(None, alias="logo_url")
    category: Optional[str] = None
    is_active: bool = Field(default=True, alias="is_active")
    is_featured: bool = Field(default=False, alias="is_featured")
    rating: float = Field(default=0.0)
    review_count: int = Field(default=0, alias="review_count")
    created_at: datetime = Field(alias="created_at")
    updated_at: datetime = Field(alias="updated_at")


class CreateVendorBody(BaseModel):
    """Create vendor request."""

    model_config = ConfigDict(populate_by_name=True)

    name: str
    slug: Optional[str] = None
    description: Optional[str] = None
    email: str
    phone: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    zip_code: Optional[str] = Field(None, alias="zipCode")
    logo_url: Optional[str] = Field(None, alias="logoUrl")
    category: Optional[str] = None
    is_active: bool = Field(default=True, alias="isActive")
    is_featured: bool = Field(default=False, alias="isFeatured")


class UpdateVendorBody(BaseModel):
    """Update vendor request."""

    model_config = ConfigDict(populate_by_name=True)

    name: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    zip_code: Optional[str] = Field(None, alias="zipCode")
    logo_url: Optional[str] = Field(None, alias="logoUrl")
    category: Optional[str] = None
    is_active: Optional[bool] = Field(None, alias="isActive")
    is_featured: Optional[bool] = Field(None, alias="isFeatured")


class VendorStats(BaseModel):
    """Vendor statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total_vendors: int = Field(alias="totalVendors")
    active_vendors: int = Field(alias="activeVendors")
    featured_vendors: int = Field(alias="featuredVendors")
    average_rating: float = Field(alias="averageRating")
    total_reviews: int = Field(alias="totalReviews")
