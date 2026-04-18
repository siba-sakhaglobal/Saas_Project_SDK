"""Events module client."""

from typing import Optional
from ..client import HttpClient
from ..models import (
    Event,
    EventCategory,
    EventStats,
    CreateEventBody,
    UpdateEventBody,
    CreateEventCategoryBody,
    UpdateEventCategoryBody,
    PaginatedResponse,
)


class EventsModule:
    """Events module client."""

    def __init__(self, client: HttpClient) -> None:
        """Initialize events module.

        Args:
            client: HTTP client instance
        """
        self.client = client

    # Events
    def get_events(
        self,
        limit: int = 50,
        page: int = 1,
        search: Optional[str] = None,
    ) -> PaginatedResponse[Event]:
        """Get all events.

        Args:
            limit: Items per page
            page: Page number
            search: Search query

        Returns:
            Paginated events
        """
        data = self.client.get(
            "/api/events",
            limit=limit,
            page=page,
            search=search,
        )
        return self._parse_paginated_response(data, Event)

    async def get_events_async(
        self,
        limit: int = 50,
        page: int = 1,
        search: Optional[str] = None,
    ) -> PaginatedResponse[Event]:
        """Get all events (async).

        Args:
            limit: Items per page
            page: Page number
            search: Search query

        Returns:
            Paginated events
        """
        data = await self.client.get_async(
            "/api/events",
            limit=limit,
            page=page,
            search=search,
        )
        return self._parse_paginated_response(data, Event)

    def get_event(self, event_id: str) -> Event:
        """Get an event by ID.

        Args:
            event_id: Event ID

        Returns:
            Event
        """
        data = self.client.get(f"/api/events/{event_id}")
        return Event(**data)

    async def get_event_async(self, event_id: str) -> Event:
        """Get an event by ID (async).

        Args:
            event_id: Event ID

        Returns:
            Event
        """
        data = await self.client.get_async(f"/api/events/{event_id}")
        return Event(**data)

    def create_event(self, body: CreateEventBody) -> Event:
        """Create an event.

        Args:
            body: Create event request

        Returns:
            Created event
        """
        data = self.client.post(
            "/api/events",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Event(**data)

    async def create_event_async(self, body: CreateEventBody) -> Event:
        """Create an event (async).

        Args:
            body: Create event request

        Returns:
            Created event
        """
        data = await self.client.post_async(
            "/api/events",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Event(**data)

    def update_event(self, event_id: str, body: UpdateEventBody) -> Event:
        """Update an event.

        Args:
            event_id: Event ID
            body: Update event request

        Returns:
            Updated event
        """
        data = self.client.put(
            f"/api/events/{event_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Event(**data)

    async def update_event_async(self, event_id: str, body: UpdateEventBody) -> Event:
        """Update an event (async).

        Args:
            event_id: Event ID
            body: Update event request

        Returns:
            Updated event
        """
        data = await self.client.put_async(
            f"/api/events/{event_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Event(**data)

    def delete_event(self, event_id: str) -> None:
        """Delete an event.

        Args:
            event_id: Event ID
        """
        self.client.delete(f"/api/events/{event_id}")

    async def delete_event_async(self, event_id: str) -> None:
        """Delete an event (async).

        Args:
            event_id: Event ID
        """
        await self.client.delete_async(f"/api/events/{event_id}")

    # Event Categories
    def get_categories(
        self,
        limit: int = 50,
        page: int = 1,
    ) -> PaginatedResponse[EventCategory]:
        """Get all event categories.

        Args:
            limit: Items per page
            page: Page number

        Returns:
            Paginated event categories
        """
        data = self.client.get(
            "/api/events/categories",
            limit=limit,
            page=page,
        )
        return self._parse_paginated_response(data, EventCategory)

    async def get_categories_async(
        self,
        limit: int = 50,
        page: int = 1,
    ) -> PaginatedResponse[EventCategory]:
        """Get all event categories (async).

        Args:
            limit: Items per page
            page: Page number

        Returns:
            Paginated event categories
        """
        data = await self.client.get_async(
            "/api/events/categories",
            limit=limit,
            page=page,
        )
        return self._parse_paginated_response(data, EventCategory)

    def get_category(self, category_id: str) -> EventCategory:
        """Get an event category by ID.

        Args:
            category_id: Category ID

        Returns:
            Event category
        """
        data = self.client.get(f"/api/events/categories/{category_id}")
        return EventCategory(**data)

    async def get_category_async(self, category_id: str) -> EventCategory:
        """Get an event category by ID (async).

        Args:
            category_id: Category ID

        Returns:
            Event category
        """
        data = await self.client.get_async(f"/api/events/categories/{category_id}")
        return EventCategory(**data)

    def create_category(self, body: CreateEventCategoryBody) -> EventCategory:
        """Create an event category.

        Args:
            body: Create category request

        Returns:
            Created event category
        """
        data = self.client.post(
            "/api/events/categories",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return EventCategory(**data)

    async def create_category_async(self, body: CreateEventCategoryBody) -> EventCategory:
        """Create an event category (async).

        Args:
            body: Create category request

        Returns:
            Created event category
        """
        data = await self.client.post_async(
            "/api/events/categories",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return EventCategory(**data)

    def update_category(self, category_id: str, body: UpdateEventCategoryBody) -> EventCategory:
        """Update an event category.

        Args:
            category_id: Category ID
            body: Update category request

        Returns:
            Updated event category
        """
        data = self.client.put(
            f"/api/events/categories/{category_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return EventCategory(**data)

    async def update_category_async(
        self, category_id: str, body: UpdateEventCategoryBody
    ) -> EventCategory:
        """Update an event category (async).

        Args:
            category_id: Category ID
            body: Update category request

        Returns:
            Updated event category
        """
        data = await self.client.put_async(
            f"/api/events/categories/{category_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return EventCategory(**data)

    def delete_category(self, category_id: str) -> None:
        """Delete an event category.

        Args:
            category_id: Category ID
        """
        self.client.delete(f"/api/events/categories/{category_id}")

    async def delete_category_async(self, category_id: str) -> None:
        """Delete an event category (async).

        Args:
            category_id: Category ID
        """
        await self.client.delete_async(f"/api/events/categories/{category_id}")

    # Event Stats
    def get_stats(self) -> EventStats:
        """Get event statistics.

        Returns:
            Event statistics
        """
        data = self.client.get("/api/events/stats")
        return EventStats(**data)

    async def get_stats_async(self) -> EventStats:
        """Get event statistics (async).

        Returns:
            Event statistics
        """
        data = await self.client.get_async("/api/events/stats")
        return EventStats(**data)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
