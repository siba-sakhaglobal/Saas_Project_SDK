"""Orders module client."""

from typing import Optional
from ..client import HttpClient
from ..models import Order, CreateOrderBody, UpdateOrderBody, OrderStats, PaginatedResponse


class OrdersModule:
    """Orders module client."""

    def __init__(self, client: HttpClient) -> None:
        self.client = client

    def get_orders(
        self, limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Order]:
        """Get all orders."""
        data = self.client.get(
            "/api/project-orders", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Order)

    async def get_orders_async(
        self, limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Order]:
        """Get all orders (async)."""
        data = await self.client.get_async(
            "/api/project-orders", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Order)

    def get_order(self, order_id: str) -> Order:
        """Get an order by ID."""
        data = self.client.get(f"/api/project-orders/{order_id}")
        return Order(**data)

    async def get_order_async(self, order_id: str) -> Order:
        """Get an order by ID (async)."""
        data = await self.client.get_async(f"/api/project-orders/{order_id}")
        return Order(**data)

    def create_order(self, body: CreateOrderBody) -> Order:
        """Create an order."""
        data = self.client.post(
            "/api/project-orders",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Order(**data)

    async def create_order_async(self, body: CreateOrderBody) -> Order:
        """Create an order (async)."""
        data = await self.client.post_async(
            "/api/project-orders",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Order(**data)

    def update_order(self, order_id: str, body: UpdateOrderBody) -> Order:
        """Update an order."""
        data = self.client.put(
            f"/api/project-orders/{order_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Order(**data)

    async def update_order_async(self, order_id: str, body: UpdateOrderBody) -> Order:
        """Update an order (async)."""
        data = await self.client.put_async(
            f"/api/project-orders/{order_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Order(**data)

    def delete_order(self, order_id: str) -> None:
        """Delete an order."""
        self.client.delete(f"/api/project-orders/{order_id}")

    async def delete_order_async(self, order_id: str) -> None:
        """Delete an order (async)."""
        await self.client.delete_async(f"/api/project-orders/{order_id}")

    def get_stats(self) -> OrderStats:
        """Get order statistics."""
        data = self.client.get("/api/project-orders/stats")
        return OrderStats(**data)

    async def get_stats_async(self) -> OrderStats:
        """Get order statistics (async)."""
        data = await self.client.get_async("/api/project-orders/stats")
        return OrderStats(**data)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
