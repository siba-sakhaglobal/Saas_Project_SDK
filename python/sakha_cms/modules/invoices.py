"""Invoices module client."""

from typing import Optional
from ..client import HttpClient
from ..models import Invoice, CreateInvoiceBody, UpdateInvoiceBody, InvoiceStats, PaginatedResponse


class InvoicesModule:
    """Invoices module client."""

    def __init__(self, client: HttpClient) -> None:
        self.client = client

    def get_invoices(
        self,  limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Invoice]:
        """Get all invoices."""
        data = self.client.get(
            f"/api/project-invoices", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Invoice)

    async def get_invoices_async(
        self,  limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Invoice]:
        """Get all invoices (async)."""
        data = await self.client.get_async(
            f"/api/project-invoices", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Invoice)

    def get_invoice(self,  invoice_id: str) -> Invoice:
        """Get an invoice by ID."""
        data = self.client.get(f"/api/project-invoices/{invoice_id}")
        return Invoice(**data)

    async def get_invoice_async(self,  invoice_id: str) -> Invoice:
        """Get an invoice by ID (async)."""
        data = await self.client.get_async(f"/api/project-invoices/{invoice_id}")
        return Invoice(**data)

    def create_invoice(self, body: CreateInvoiceBody) -> Invoice:
        """Create an invoice."""
        data = self.client.post(
            "/api/project-invoices",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Invoice(**data)

    async def create_invoice_async(self, body: CreateInvoiceBody) -> Invoice:
        """Create an invoice (async)."""
        data = await self.client.post_async(
            "/api/project-invoices",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Invoice(**data)

    def update_invoice(
        self,  invoice_id: str, body: UpdateInvoiceBody
    ) -> Invoice:
        """Update an invoice."""
        data = self.client.put(
            f"/api/project-invoices/{invoice_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Invoice(**data)

    async def update_invoice_async(
        self,  invoice_id: str, body: UpdateInvoiceBody
    ) -> Invoice:
        """Update an invoice (async)."""
        data = await self.client.put_async(
            f"/api/project-invoices/{invoice_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Invoice(**data)

    def delete_invoice(self,  invoice_id: str) -> None:
        """Delete an invoice."""
        self.client.delete(f"/api/project-invoices/{invoice_id}")

    async def delete_invoice_async(self,  invoice_id: str) -> None:
        """Delete an invoice (async)."""
        await self.client.delete_async(f"/api/project-invoices/{invoice_id}")

    def get_stats(self, ) -> InvoiceStats:
        """Get invoice statistics."""
        data = self.client.get(f"/api/project-invoices/stats")
        return InvoiceStats(**data)

    async def get_stats_async(self, ) -> InvoiceStats:
        """Get invoice statistics (async)."""
        data = await self.client.get_async(f"/api/project-invoices/stats")
        return InvoiceStats(**data)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
