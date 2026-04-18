"""Team module client."""

from typing import Optional
from ..client import HttpClient
from ..models import TeamMember, CreateTeamMemberBody, UpdateTeamMemberBody, TeamStats, PaginatedResponse


class TeamModule:
    """Team module client."""

    def __init__(self, client: HttpClient) -> None:
        self.client = client

    def get_members(
        self,  limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[TeamMember]:
        """Get all team members."""
        data = self.client.get(
            f"/api/team", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, TeamMember)

    async def get_members_async(
        self,  limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[TeamMember]:
        """Get all team members (async)."""
        data = await self.client.get_async(
            f"/api/team", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, TeamMember)

    def get_member(self,  member_id: str) -> TeamMember:
        """Get a team member by ID."""
        data = self.client.get(f"/api/team/{member_id}")
        return TeamMember(**data)

    async def get_member_async(self,  member_id: str) -> TeamMember:
        """Get a team member by ID (async)."""
        data = await self.client.get_async(f"/api/team/{member_id}")
        return TeamMember(**data)

    def create_member(self, body: CreateTeamMemberBody) -> TeamMember:
        """Create a team member."""
        data = self.client.post(
            "/api/team",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return TeamMember(**data)

    async def create_member_async(self, body: CreateTeamMemberBody) -> TeamMember:
        """Create a team member (async)."""
        data = await self.client.post_async(
            "/api/team",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return TeamMember(**data)

    def update_member(
        self,  member_id: str, body: UpdateTeamMemberBody
    ) -> TeamMember:
        """Update a team member."""
        data = self.client.put(
            f"/api/team/{member_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return TeamMember(**data)

    async def update_member_async(
        self,  member_id: str, body: UpdateTeamMemberBody
    ) -> TeamMember:
        """Update a team member (async)."""
        data = await self.client.put_async(
            f"/api/team/{member_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return TeamMember(**data)

    def delete_member(self,  member_id: str) -> None:
        """Delete a team member."""
        self.client.delete(f"/api/team/{member_id}")

    async def delete_member_async(self,  member_id: str) -> None:
        """Delete a team member (async)."""
        await self.client.delete_async(f"/api/team/{member_id}")

    def get_stats(self, ) -> TeamStats:
        """Get team statistics."""
        data = self.client.get(f"/api/team/stats")
        return TeamStats(**data)

    async def get_stats_async(self, ) -> TeamStats:
        """Get team statistics (async)."""
        data = await self.client.get_async(f"/api/team/stats")
        return TeamStats(**data)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
