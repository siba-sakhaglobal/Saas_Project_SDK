"""Products module client."""

from typing import Optional
from ..client import HttpClient
from ..models import Product, CreateProductBody, UpdateProductBody, ProductStats, PaginatedResponse


class ProductsModule:
    """Products module client."""

    def __init__(self, client: HttpClient) -> None:
        self.client = client

    def get_products(
        self, limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Product]:
        """Get all products."""
        data = self.client.get(
            "/api/project-products", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Product)

    async def get_products_async(
        self, limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Product]:
        """Get all products (async)."""
        data = await self.client.get_async(
            "/api/project-products", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Product)

    def get_product(self, product_id: str) -> Product:
        """Get a product by ID."""
        data = self.client.get(f"/api/project-products/{product_id}")
        return Product(**data)

    async def get_product_async(self, product_id: str) -> Product:
        """Get a product by ID (async)."""
        data = await self.client.get_async(f"/api/project-products/{product_id}")
        return Product(**data)

    def create_product(self, body: CreateProductBody) -> Product:
        """Create a product."""
        data = self.client.post(
            "/api/project-products",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Product(**data)

    async def create_product_async(self, body: CreateProductBody) -> Product:
        """Create a product (async)."""
        data = await self.client.post_async(
            "/api/project-products",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Product(**data)

    def update_product(self, product_id: str, body: UpdateProductBody) -> Product:
        """Update a product."""
        data = self.client.put(
            f"/api/project-products/{product_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Product(**data)

    async def update_product_async(
        self, product_id: str, body: UpdateProductBody
    ) -> Product:
        """Update a product (async)."""
        data = await self.client.put_async(
            f"/api/project-products/{product_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Product(**data)

    def delete_product(self, product_id: str) -> None:
        """Delete a product."""
        self.client.delete(f"/api/project-products/{product_id}")

    async def delete_product_async(self, product_id: str) -> None:
        """Delete a product (async)."""
        await self.client.delete_async(f"/api/project-products/{product_id}")

    def get_stats(self) -> ProductStats:
        """Get product statistics."""
        data = self.client.get("/api/project-products/stats")
        return ProductStats(**data)

    async def get_stats_async(self) -> ProductStats:
        """Get product statistics (async)."""
        data = await self.client.get_async("/api/project-products/stats")
        return ProductStats(**data)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
