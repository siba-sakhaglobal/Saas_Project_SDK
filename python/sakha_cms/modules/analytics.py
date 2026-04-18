"""Analytics module client."""

from typing import Optional
from ..client import HttpClient
from ..models import AnalyticsStats, TrafficStats, PaginatedResponse


class AnalyticsModule:
    """Analytics module client."""

    def __init__(self, client: HttpClient) -> None:
        self.client = client

    def get_stats(self, ) -> AnalyticsStats:
        """Get analytics statistics."""
        data = self.client.get(f"/api/analytics/stats")
        return AnalyticsStats(**data)

    async def get_stats_async(self, ) -> AnalyticsStats:
        """Get analytics statistics (async)."""
        data = await self.client.get_async(f"/api/analytics/stats")
        return AnalyticsStats(**data)

    def get_traffic(
        self,
        
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        limit: int = 50,
        page: int = 1,
    ) -> PaginatedResponse[TrafficStats]:
        """Get traffic statistics."""
        data = self.client.get(
            f"/api/analytics/traffic",
            start_date=start_date,
            end_date=end_date,
            limit=limit,
            page=page,
        )
        return self._parse_paginated_response(data, TrafficStats)

    async def get_traffic_async(
        self,
        
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        limit: int = 50,
        page: int = 1,
    ) -> PaginatedResponse[TrafficStats]:
        """Get traffic statistics (async)."""
        data = await self.client.get_async(
            f"/api/analytics/traffic",
            start_date=start_date,
            end_date=end_date,
            limit=limit,
            page=page,
        )
        return self._parse_paginated_response(data, TrafficStats)

    def get_page_views(
        self,
        
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        limit: int = 50,
        page: int = 1,
    ) -> PaginatedResponse:
        """Get page views."""
        data = self.client.get(
            f"/api/analytics/page-views",
            start_date=start_date,
            end_date=end_date,
            limit=limit,
            page=page,
        )
        return self._parse_paginated_response(data, dict)

    async def get_page_views_async(
        self,
        
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        limit: int = 50,
        page: int = 1,
    ) -> PaginatedResponse:
        """Get page views (async)."""
        data = await self.client.get_async(
            f"/api/analytics/page-views",
            start_date=start_date,
            end_date=end_date,
            limit=limit,
            page=page,
        )
        return self._parse_paginated_response(data, dict)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            if model == dict:
                items = data.get("items", [])
            else:
                items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
