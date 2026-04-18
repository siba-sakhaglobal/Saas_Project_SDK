"""Shipments module client."""

from typing import Optional
from ..client import HttpClient
from ..models import Shipment, CreateShipmentBody, UpdateShipmentBody, ShipmentStats, PaginatedResponse


class ShipmentsModule:
    """Shipments module client."""

    def __init__(self, client: HttpClient) -> None:
        self.client = client

    def get_shipments(
        self,  limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Shipment]:
        """Get all shipments."""
        data = self.client.get(
            f"/api/project-shipments", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Shipment)

    async def get_shipments_async(
        self,  limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Shipment]:
        """Get all shipments (async)."""
        data = await self.client.get_async(
            f"/api/project-shipments", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Shipment)

    def get_shipment(self,  shipment_id: str) -> Shipment:
        """Get a shipment by ID."""
        data = self.client.get(f"/api/project-shipments/{shipment_id}")
        return Shipment(**data)

    async def get_shipment_async(self,  shipment_id: str) -> Shipment:
        """Get a shipment by ID (async)."""
        data = await self.client.get_async(f"/api/project-shipments/{shipment_id}")
        return Shipment(**data)

    def create_shipment(self, body: CreateShipmentBody) -> Shipment:
        """Create a shipment."""
        data = self.client.post(
            "/api/project-shipments",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Shipment(**data)

    async def create_shipment_async(self, body: CreateShipmentBody) -> Shipment:
        """Create a shipment (async)."""
        data = await self.client.post_async(
            "/api/project-shipments",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Shipment(**data)

    def update_shipment(
        self,  shipment_id: str, body: UpdateShipmentBody
    ) -> Shipment:
        """Update a shipment."""
        data = self.client.put(
            f"/api/project-shipments/{shipment_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Shipment(**data)

    async def update_shipment_async(
        self,  shipment_id: str, body: UpdateShipmentBody
    ) -> Shipment:
        """Update a shipment (async)."""
        data = await self.client.put_async(
            f"/api/project-shipments/{shipment_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Shipment(**data)

    def delete_shipment(self,  shipment_id: str) -> None:
        """Delete a shipment."""
        self.client.delete(f"/api/project-shipments/{shipment_id}")

    async def delete_shipment_async(self,  shipment_id: str) -> None:
        """Delete a shipment (async)."""
        await self.client.delete_async(f"/api/project-shipments/{shipment_id}")

    def get_stats(self, ) -> ShipmentStats:
        """Get shipment statistics."""
        data = self.client.get(f"/api/project-shipments/stats")
        return ShipmentStats(**data)

    async def get_stats_async(self, ) -> ShipmentStats:
        """Get shipment statistics (async)."""
        data = await self.client.get_async(f"/api/project-shipments/stats")
        return ShipmentStats(**data)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
