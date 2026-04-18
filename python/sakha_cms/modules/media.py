"""Media module client."""

from typing import Optional
from ..client import HttpClient
from ..models import Media, CreateMediaBody, UpdateMediaBody, MediaStats, PaginatedResponse


class MediaModule:
    """Media module client."""

    def __init__(self, client: HttpClient) -> None:
        self.client = client

    def get_media(
        self,  limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Media]:
        """Get all media files."""
        data = self.client.get(
            f"/api/media", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Media)

    async def get_media_async(
        self,  limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Media]:
        """Get all media files (async)."""
        data = await self.client.get_async(
            f"/api/media", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Media)

    def get_media_file(self,  media_id: str) -> Media:
        """Get a media file by ID."""
        data = self.client.get(f"/api/media/{media_id}")
        return Media(**data)

    async def get_media_file_async(self,  media_id: str) -> Media:
        """Get a media file by ID (async)."""
        data = await self.client.get_async(f"/api/media/{media_id}")
        return Media(**data)

    def create_media(self, body: CreateMediaBody) -> Media:
        """Create a media file."""
        data = self.client.post(
            "/api/media",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Media(**data)

    async def create_media_async(self, body: CreateMediaBody) -> Media:
        """Create a media file (async)."""
        data = await self.client.post_async(
            "/api/media",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Media(**data)

    def update_media(self,  media_id: str, body: UpdateMediaBody) -> Media:
        """Update a media file."""
        data = self.client.put(
            f"/api/media/{media_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Media(**data)

    async def update_media_async(
        self,  media_id: str, body: UpdateMediaBody
    ) -> Media:
        """Update a media file (async)."""
        data = await self.client.put_async(
            f"/api/media/{media_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Media(**data)

    def delete_media(self,  media_id: str) -> None:
        """Delete a media file."""
        self.client.delete(f"/api/media/{media_id}")

    async def delete_media_async(self,  media_id: str) -> None:
        """Delete a media file (async)."""
        await self.client.delete_async(f"/api/media/{media_id}")

    def get_stats(self, ) -> MediaStats:
        """Get media statistics."""
        data = self.client.get(f"/api/media/stats")
        return MediaStats(**data)

    async def get_stats_async(self, ) -> MediaStats:
        """Get media statistics (async)."""
        data = await self.client.get_async(f"/api/media/stats")
        return MediaStats(**data)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
