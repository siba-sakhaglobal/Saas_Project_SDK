"""Services module client."""

from typing import Optional
from ..client import HttpClient
from ..models import Service, CreateServiceBody, UpdateServiceBody, ServiceStats, PaginatedResponse


class ServicesModule:
    """Services module client."""

    def __init__(self, client: HttpClient) -> None:
        self.client = client

    def get_services(
        self, limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Service]:
        """Get all services."""
        data = self.client.get(
            "/api/project-services", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Service)

    async def get_services_async(
        self, limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Service]:
        """Get all services (async)."""
        data = await self.client.get_async(
            "/api/project-services", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Service)

    def get_service(self, service_id: str) -> Service:
        """Get a service by ID."""
        data = self.client.get(f"/api/project-services/{service_id}")
        return Service(**data)

    async def get_service_async(self, service_id: str) -> Service:
        """Get a service by ID (async)."""
        data = await self.client.get_async(f"/api/project-services/{service_id}")
        return Service(**data)

    def create_service(self, body: CreateServiceBody) -> Service:
        """Create a service."""
        data = self.client.post(
            "/api/project-services",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Service(**data)

    async def create_service_async(self, body: CreateServiceBody) -> Service:
        """Create a service (async)."""
        data = await self.client.post_async(
            "/api/project-services",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Service(**data)

    def update_service(self, service_id: str, body: UpdateServiceBody) -> Service:
        """Update a service."""
        data = self.client.put(
            f"/api/project-services/{service_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Service(**data)

    async def update_service_async(
        self, service_id: str, body: UpdateServiceBody
    ) -> Service:
        """Update a service (async)."""
        data = await self.client.put_async(
            f"/api/project-services/{service_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Service(**data)

    def delete_service(self, service_id: str) -> None:
        """Delete a service."""
        self.client.delete(f"/api/project-services/{service_id}")

    async def delete_service_async(self, service_id: str) -> None:
        """Delete a service (async)."""
        await self.client.delete_async(f"/api/project-services/{service_id}")

    def get_stats(self) -> ServiceStats:
        """Get service statistics."""
        data = self.client.get("/api/project-services/stats")
        return ServiceStats(**data)

    async def get_stats_async(self) -> ServiceStats:
        """Get service statistics (async)."""
        data = await self.client.get_async("/api/project-services/stats")
        return ServiceStats(**data)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
