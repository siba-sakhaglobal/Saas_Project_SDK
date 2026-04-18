"""Vendors module client."""

from typing import Optional
from ..client import HttpClient
from ..models import Vendor, CreateVendorBody, UpdateVendorBody, VendorStats, PaginatedResponse


class VendorsModule:
    """Vendors module client."""

    def __init__(self, client: HttpClient) -> None:
        self.client = client

    def get_vendors(
        self,  limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Vendor]:
        """Get all vendors."""
        data = self.client.get(
            f"/api/project-vendors", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Vendor)

    async def get_vendors_async(
        self,  limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Vendor]:
        """Get all vendors (async)."""
        data = await self.client.get_async(
            f"/api/project-vendors", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Vendor)

    def get_vendor(self,  vendor_id: str) -> Vendor:
        """Get a vendor by ID."""
        data = self.client.get(f"/api/project-vendors/{vendor_id}")
        return Vendor(**data)

    async def get_vendor_async(self,  vendor_id: str) -> Vendor:
        """Get a vendor by ID (async)."""
        data = await self.client.get_async(f"/api/project-vendors/{vendor_id}")
        return Vendor(**data)

    def create_vendor(self, body: CreateVendorBody) -> Vendor:
        """Create a vendor."""
        data = self.client.post(
            "/api/project-vendors",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Vendor(**data)

    async def create_vendor_async(self, body: CreateVendorBody) -> Vendor:
        """Create a vendor (async)."""
        data = await self.client.post_async(
            "/api/project-vendors",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Vendor(**data)

    def update_vendor(self,  vendor_id: str, body: UpdateVendorBody) -> Vendor:
        """Update a vendor."""
        data = self.client.put(
            f"/api/project-vendors/{vendor_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Vendor(**data)

    async def update_vendor_async(
        self,  vendor_id: str, body: UpdateVendorBody
    ) -> Vendor:
        """Update a vendor (async)."""
        data = await self.client.put_async(
            f"/api/project-vendors/{vendor_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Vendor(**data)

    def delete_vendor(self,  vendor_id: str) -> None:
        """Delete a vendor."""
        self.client.delete(f"/api/project-vendors/{vendor_id}")

    async def delete_vendor_async(self,  vendor_id: str) -> None:
        """Delete a vendor (async)."""
        await self.client.delete_async(f"/api/project-vendors/{vendor_id}")

    def get_stats(self, ) -> VendorStats:
        """Get vendor statistics."""
        data = self.client.get(f"/api/project-vendors/stats")
        return VendorStats(**data)

    async def get_stats_async(self, ) -> VendorStats:
        """Get vendor statistics (async)."""
        data = await self.client.get_async(f"/api/project-vendors/stats")
        return VendorStats(**data)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
