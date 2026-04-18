"""Blog module models."""

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional, Any


class BlogAuthor(BaseModel):
    """Blog post author."""

    model_config = ConfigDict(populate_by_name=True)

    id: Optional[str] = None
    name: str
    avatar: Optional[str] = None
    role: str = "Editor"


class BlogCategory(BaseModel):
    """Blog category."""

    model_config = ConfigDict(populate_by_name=True)

    id: Optional[str] = None
    name: str
    slug: str
    color: str = "#64748B"
    sort_order: int = Field(default=0, alias="sortOrder")


class BlogPost(BaseModel):
    """Blog post."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    slug: str
    excerpt: Optional[str] = None
    content: Optional[str] = None
    featured_image: Optional[str] = Field(None, alias="featured_image")
    status: str  # draft|published|archived
    is_featured: bool = Field(default=False, alias="is_featured")
    author: BlogAuthor
    category: Optional[BlogCategory] = None
    category_name: Optional[str] = None
    tags: list[str] = Field(default_factory=list)
    view_count: int = Field(default=0, alias="viewCount")
    comment_count: int = Field(default=0, alias="commentCount")
    share_count: int = Field(default=0, alias="shareCount")
    published_at: Optional[datetime] = Field(None, alias="published_at")
    created_at: datetime = Field(alias="created_at")
    updated_at: datetime = Field(alias="updated_at")


class CreateBlogPostBody(BaseModel):
    """Create blog post request."""

    model_config = ConfigDict(populate_by_name=True)

    title: str
    slug: Optional[str] = None
    excerpt: Optional[str] = None
    content: Optional[str] = None
    featured_image: Optional[str] = Field(None, alias="featured_image")
    status: str = "draft"
    tags: Optional[list[str]] = None
    is_featured: bool = Field(default=False, alias="is_featured")
    published_at: Optional[datetime] = Field(None, alias="published_at")
    author_name: Optional[str] = Field(None, alias="author_name")


class UpdateBlogPostBody(BaseModel):
    """Update blog post request."""

    model_config = ConfigDict(populate_by_name=True)

    title: Optional[str] = None
    slug: Optional[str] = None
    excerpt: Optional[str] = None
    content: Optional[str] = None
    featured_image: Optional[str] = Field(None, alias="featured_image")
    status: Optional[str] = None
    tags: Optional[list[str]] = None
    is_featured: Optional[bool] = Field(None, alias="is_featured")
    published_at: Optional[datetime] = Field(None, alias="published_at")
    author_name: Optional[str] = Field(None, alias="author_name")


class CreateBlogCategoryBody(BaseModel):
    """Create blog category request."""

    model_config = ConfigDict(populate_by_name=True)

    name: str
    slug: Optional[str] = None
    color: str = "#64748B"
    sort_order: int = Field(default=0, alias="sortOrder")


class UpdateBlogCategoryBody(BaseModel):
    """Update blog category request."""

    model_config = ConfigDict(populate_by_name=True)

    name: Optional[str] = None
    slug: Optional[str] = None
    color: Optional[str] = None
    sort_order: Optional[int] = Field(None, alias="sortOrder")


class BlogAuthorResponse(BaseModel):
    """Blog author in list."""

    model_config = ConfigDict(populate_by_name=True)

    id: int
    name: str
    role: str


class BlogStats(BaseModel):
    """Blog statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total: int
    published: int
    drafts: int
    archived: int
