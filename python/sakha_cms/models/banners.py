"""Banners module models."""

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class Banner(BaseModel):
    """Banner."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    project_id: Optional[str] = Field(None, alias="project_id")
    title: str
    slug: str
    description: Optional[str] = None
    image_url: Optional[str] = Field(None, alias="image_url")
    link_url: Optional[str] = Field(None, alias="link_url")
    link_text: Optional[str] = Field(None, alias="link_text")
    position: Optional[str] = None  # top|middle|bottom
    is_active: bool = Field(default=True, alias="is_active")
    is_featured: bool = Field(default=False, alias="is_featured")
    start_date: Optional[datetime] = Field(None, alias="start_date")
    end_date: Optional[datetime] = Field(None, alias="end_date")
    sort_order: int = Field(default=0, alias="sort_order")
    created_at: datetime = Field(alias="created_at")
    updated_at: datetime = Field(alias="updated_at")


class CreateBannerBody(BaseModel):
    """Create banner request."""

    model_config = ConfigDict(populate_by_name=True)

    title: str
    slug: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = Field(None, alias="imageUrl")
    link_url: Optional[str] = Field(None, alias="linkUrl")
    link_text: Optional[str] = Field(None, alias="linkText")
    position: Optional[str] = None
    is_active: bool = Field(default=True, alias="isActive")
    is_featured: bool = Field(default=False, alias="isFeatured")
    start_date: Optional[datetime] = Field(None, alias="startDate")
    end_date: Optional[datetime] = Field(None, alias="endDate")
    sort_order: int = Field(default=0, alias="sortOrder")


class UpdateBannerBody(BaseModel):
    """Update banner request."""

    model_config = ConfigDict(populate_by_name=True)

    title: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = Field(None, alias="imageUrl")
    link_url: Optional[str] = Field(None, alias="linkUrl")
    link_text: Optional[str] = Field(None, alias="linkText")
    position: Optional[str] = None
    is_active: Optional[bool] = Field(None, alias="isActive")
    is_featured: Optional[bool] = Field(None, alias="isFeatured")
    start_date: Optional[datetime] = Field(None, alias="startDate")
    end_date: Optional[datetime] = Field(None, alias="endDate")
    sort_order: Optional[int] = Field(None, alias="sortOrder")


class BannerStats(BaseModel):
    """Banner statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total_banners: int = Field(alias="totalBanners")
    active_banners: int = Field(alias="activeBanners")
    featured_banners: int = Field(alias="featuredBanners")
    total_clicks: int = Field(alias="totalClicks")
    total_impressions: int = Field(alias="totalImpressions")
