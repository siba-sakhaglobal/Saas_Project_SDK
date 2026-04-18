"""User Groups module client."""

from typing import Optional
from ..client import HttpClient
from ..models import UserGroup, CreateUserGroupBody, UpdateUserGroupBody, UserGroupStats, PaginatedResponse


class UserGroupsModule:
    """User Groups module client."""

    def __init__(self, client: HttpClient) -> None:
        self.client = client

    def get_groups(
        self,  limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[UserGroup]:
        """Get all user groups."""
        data = self.client.get(
            f"/api/user-groups", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, UserGroup)

    async def get_groups_async(
        self,  limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[UserGroup]:
        """Get all user groups (async)."""
        data = await self.client.get_async(
            f"/api/user-groups", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, UserGroup)

    def get_group(self,  group_id: str) -> UserGroup:
        """Get a user group by ID."""
        data = self.client.get(f"/api/user-groups/{group_id}")
        return UserGroup(**data)

    async def get_group_async(self,  group_id: str) -> UserGroup:
        """Get a user group by ID (async)."""
        data = await self.client.get_async(f"/api/user-groups/{group_id}")
        return UserGroup(**data)

    def create_group(self, body: CreateUserGroupBody) -> UserGroup:
        """Create a user group."""
        data = self.client.post(
            "/api/user-groups",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return UserGroup(**data)

    async def create_group_async(self, body: CreateUserGroupBody) -> UserGroup:
        """Create a user group (async)."""
        data = await self.client.post_async(
            "/api/user-groups",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return UserGroup(**data)

    def update_group(
        self,  group_id: str, body: UpdateUserGroupBody
    ) -> UserGroup:
        """Update a user group."""
        data = self.client.put(
            f"/api/user-groups/{group_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return UserGroup(**data)

    async def update_group_async(
        self,  group_id: str, body: UpdateUserGroupBody
    ) -> UserGroup:
        """Update a user group (async)."""
        data = await self.client.put_async(
            f"/api/user-groups/{group_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return UserGroup(**data)

    def delete_group(self,  group_id: str) -> None:
        """Delete a user group."""
        self.client.delete(f"/api/user-groups/{group_id}")

    async def delete_group_async(self,  group_id: str) -> None:
        """Delete a user group (async)."""
        await self.client.delete_async(f"/api/user-groups/{group_id}")

    def get_stats(self, ) -> UserGroupStats:
        """Get user group statistics."""
        data = self.client.get(f"/api/user-groups/stats")
        return UserGroupStats(**data)

    async def get_stats_async(self, ) -> UserGroupStats:
        """Get user group statistics (async)."""
        data = await self.client.get_async(f"/api/user-groups/stats")
        return UserGroupStats(**data)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
