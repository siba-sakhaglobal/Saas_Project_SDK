"""Banners module client."""

from typing import Optional
from ..client import HttpClient
from ..models import Banner, CreateBannerBody, UpdateBannerBody, BannerStats, PaginatedResponse


class BannersModule:
    """Banners module client."""

    def __init__(self, client: HttpClient) -> None:
        self.client = client

    def get_banners(
        self,  limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Banner]:
        """Get all banners."""
        data = self.client.get(
            f"/api/project-banners", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Banner)

    async def get_banners_async(
        self,  limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Banner]:
        """Get all banners (async)."""
        data = await self.client.get_async(
            f"/api/project-banners", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Banner)

    def get_banner(self,  banner_id: str) -> Banner:
        """Get a banner by ID."""
        data = self.client.get(f"/api/project-banners/{banner_id}")
        return Banner(**data)

    async def get_banner_async(self,  banner_id: str) -> Banner:
        """Get a banner by ID (async)."""
        data = await self.client.get_async(f"/api/project-banners/{banner_id}")
        return Banner(**data)

    def create_banner(self, body: CreateBannerBody) -> Banner:
        """Create a banner."""
        data = self.client.post(
            "/api/project-banners",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Banner(**data)

    async def create_banner_async(self, body: CreateBannerBody) -> Banner:
        """Create a banner (async)."""
        data = await self.client.post_async(
            "/api/project-banners",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Banner(**data)

    def update_banner(self,  banner_id: str, body: UpdateBannerBody) -> Banner:
        """Update a banner."""
        data = self.client.put(
            f"/api/project-banners/{banner_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Banner(**data)

    async def update_banner_async(
        self,  banner_id: str, body: UpdateBannerBody
    ) -> Banner:
        """Update a banner (async)."""
        data = await self.client.put_async(
            f"/api/project-banners/{banner_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Banner(**data)

    def delete_banner(self,  banner_id: str) -> None:
        """Delete a banner."""
        self.client.delete(f"/api/project-banners/{banner_id}")

    async def delete_banner_async(self,  banner_id: str) -> None:
        """Delete a banner (async)."""
        await self.client.delete_async(f"/api/project-banners/{banner_id}")

    def get_stats(self, ) -> BannerStats:
        """Get banner statistics."""
        data = self.client.get(f"/api/project-banners/stats")
        return BannerStats(**data)

    async def get_stats_async(self, ) -> BannerStats:
        """Get banner statistics (async)."""
        data = await self.client.get_async(f"/api/project-banners/stats")
        return BannerStats(**data)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
