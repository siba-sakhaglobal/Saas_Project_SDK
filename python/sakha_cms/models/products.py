"""Products module models."""

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class Product(BaseModel):
    """Product."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    project_id: Optional[str] = Field(None, alias="project_id")
    name: str
    slug: str
    description: Optional[str] = None
    price: float
    cost_price: Optional[float] = Field(None, alias="cost_price")
    discount_price: Optional[float] = Field(None, alias="discount_price")
    stock_quantity: int = Field(default=0, alias="stock_quantity")
    sku: Optional[str] = None
    category: Optional[str] = None
    image_url: Optional[str] = Field(None, alias="image_url")
    featured_image: Optional[str] = Field(None, alias="featured_image")
    is_active: bool = Field(default=True, alias="is_active")
    is_featured: bool = Field(default=False, alias="is_featured")
    rating: float = Field(default=0.0)
    review_count: int = Field(default=0, alias="review_count")
    view_count: int = Field(default=0, alias="view_count")
    tags: list[str] = Field(default_factory=list)
    created_at: datetime = Field(alias="created_at")
    updated_at: datetime = Field(alias="updated_at")


class CreateProductBody(BaseModel):
    """Create product request."""

    model_config = ConfigDict(populate_by_name=True)

    name: str
    slug: Optional[str] = None
    description: Optional[str] = None
    price: float
    cost_price: Optional[float] = Field(None, alias="costPrice")
    discount_price: Optional[float] = Field(None, alias="discountPrice")
    stock_quantity: int = Field(default=0, alias="stockQuantity")
    sku: Optional[str] = None
    category: Optional[str] = None
    image_url: Optional[str] = Field(None, alias="imageUrl")
    featured_image: Optional[str] = Field(None, alias="featuredImage")
    is_active: bool = Field(default=True, alias="isActive")
    is_featured: bool = Field(default=False, alias="isFeatured")
    tags: Optional[list[str]] = None


class UpdateProductBody(BaseModel):
    """Update product request."""

    model_config = ConfigDict(populate_by_name=True)

    name: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    cost_price: Optional[float] = Field(None, alias="costPrice")
    discount_price: Optional[float] = Field(None, alias="discountPrice")
    stock_quantity: Optional[int] = Field(None, alias="stockQuantity")
    sku: Optional[str] = None
    category: Optional[str] = None
    image_url: Optional[str] = Field(None, alias="imageUrl")
    featured_image: Optional[str] = Field(None, alias="featuredImage")
    is_active: Optional[bool] = Field(None, alias="isActive")
    is_featured: Optional[bool] = Field(None, alias="isFeatured")
    tags: Optional[list[str]] = None


class ProductStats(BaseModel):
    """Product statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total_products: int = Field(alias="totalProducts")
    active_products: int = Field(alias="activeProducts")
    featured_products: int = Field(alias="featuredProducts")
    total_stock: int = Field(alias="totalStock")
    out_of_stock_count: int = Field(alias="outOfStockCount")
    average_price: float = Field(alias="averagePrice")
    average_rating: float = Field(alias="averageRating")
    total_reviews: int = Field(alias="totalReviews")
    total_views: int = Field(alias="totalViews")
