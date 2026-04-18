"""Users module client."""

from typing import Optional
from ..client import HttpClient
from ..models import User, CreateUserBody, UpdateUserBody, UserStats, PaginatedResponse


class UsersModule:
    """Users module client."""

    def __init__(self, client: HttpClient) -> None:
        self.client = client

    def get_users(
        self, limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[User]:
        """Get all users."""
        data = self.client.get("/api/users", limit=limit, page=page, search=search)
        return self._parse_paginated_response(data, User)

    async def get_users_async(
        self, limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[User]:
        """Get all users (async)."""
        data = await self.client.get_async("/api/users", limit=limit, page=page, search=search)
        return self._parse_paginated_response(data, User)

    def get_user(self, user_id: str) -> User:
        """Get a user by ID."""
        data = self.client.get(f"/api/users/{user_id}")
        return User(**data)

    async def get_user_async(self, user_id: str) -> User:
        """Get a user by ID (async)."""
        data = await self.client.get_async(f"/api/users/{user_id}")
        return User(**data)

    def create_user(self, body: CreateUserBody) -> User:
        """Create a user."""
        data = self.client.post(
            "/api/users", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return User(**data)

    async def create_user_async(self, body: CreateUserBody) -> User:
        """Create a user (async)."""
        data = await self.client.post_async(
            "/api/users", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return User(**data)

    def update_user(self, user_id: str, body: UpdateUserBody) -> User:
        """Update a user."""
        data = self.client.put(
            f"/api/users/{user_id}", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return User(**data)

    async def update_user_async(self, user_id: str, body: UpdateUserBody) -> User:
        """Update a user (async)."""
        data = await self.client.put_async(
            f"/api/users/{user_id}", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return User(**data)

    def delete_user(self, user_id: str) -> None:
        """Delete a user."""
        self.client.delete(f"/api/users/{user_id}")

    async def delete_user_async(self, user_id: str) -> None:
        """Delete a user (async)."""
        await self.client.delete_async(f"/api/users/{user_id}")

    def get_stats(self) -> UserStats:
        """Get user statistics."""
        data = self.client.get("/api/users/stats")
        return UserStats(**data)

    async def get_stats_async(self) -> UserStats:
        """Get user statistics (async)."""
        data = await self.client.get_async("/api/users/stats")
        return UserStats(**data)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
