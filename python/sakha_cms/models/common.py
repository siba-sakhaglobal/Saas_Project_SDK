"""Common models for API responses."""

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, TypeVar, Generic, Optional
from datetime import datetime


class PaginatedMeta(BaseModel):
    """Pagination metadata."""

    total: int
    page: int
    limit: int


class ListParams(BaseModel):
    """Common list endpoint parameters."""

    limit: int = Field(default=50, ge=1, le=100)
    page: int = Field(default=1, ge=1)
    search: Optional[str] = None


T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    """Generic paginated response."""

    items: list[T]
    meta: PaginatedMeta


class ApiResponse(BaseModel):
    """Standard API response envelope."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
    )

    success: bool
    data: Any = None
    error: Optional[Any] = None
    meta: Optional[dict[str, Any]] = None
