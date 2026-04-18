"""Transactions module client."""

from typing import Optional
from ..client import HttpClient
from ..models import Transaction, CreateTransactionBody, UpdateTransactionBody, TransactionStats, PaginatedResponse


class TransactionsModule:
    """Transactions module client."""

    def __init__(self, client: HttpClient) -> None:
        self.client = client

    def get_transactions(
        self,  limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Transaction]:
        """Get all transactions."""
        data = self.client.get(
            f"/api/project-transactions", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Transaction)

    async def get_transactions_async(
        self,  limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Transaction]:
        """Get all transactions (async)."""
        data = await self.client.get_async(
            f"/api/project-transactions", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Transaction)

    def get_transaction(self,  transaction_id: str) -> Transaction:
        """Get a transaction by ID."""
        data = self.client.get(f"/api/project-transactions/{transaction_id}")
        return Transaction(**data)

    async def get_transaction_async(
        self,  transaction_id: str
    ) -> Transaction:
        """Get a transaction by ID (async)."""
        data = await self.client.get_async(
            f"/api/project-transactions/{transaction_id}"
        )
        return Transaction(**data)

    def create_transaction(self, body: CreateTransactionBody) -> Transaction:
        """Create a transaction."""
        data = self.client.post(
            "/api/project-transactions",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Transaction(**data)

    async def create_transaction_async(self, body: CreateTransactionBody) -> Transaction:
        """Create a transaction (async)."""
        data = await self.client.post_async(
            "/api/project-transactions",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Transaction(**data)

    def update_transaction(
        self,  transaction_id: str, body: UpdateTransactionBody
    ) -> Transaction:
        """Update a transaction."""
        data = self.client.put(
            f"/api/project-transactions/{transaction_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Transaction(**data)

    async def update_transaction_async(
        self,  transaction_id: str, body: UpdateTransactionBody
    ) -> Transaction:
        """Update a transaction (async)."""
        data = await self.client.put_async(
            f"/api/project-transactions/{transaction_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Transaction(**data)

    def delete_transaction(self,  transaction_id: str) -> None:
        """Delete a transaction."""
        self.client.delete(f"/api/project-transactions/{transaction_id}")

    async def delete_transaction_async(
        self,  transaction_id: str
    ) -> None:
        """Delete a transaction (async)."""
        await self.client.delete_async(
            f"/api/project-transactions/{transaction_id}"
        )

    def get_stats(self, ) -> TransactionStats:
        """Get transaction statistics."""
        data = self.client.get(f"/api/project-transactions/stats")
        return TransactionStats(**data)

    async def get_stats_async(self, ) -> TransactionStats:
        """Get transaction statistics (async)."""
        data = await self.client.get_async(f"/api/project-transactions/stats")
        return TransactionStats(**data)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
