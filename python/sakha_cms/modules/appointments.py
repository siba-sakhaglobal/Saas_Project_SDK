"""Appointments module client."""

from typing import Optional
from ..client import HttpClient
from ..models import Appointment, CreateAppointmentBody, UpdateAppointmentBody, AppointmentStats, PaginatedResponse


class AppointmentsModule:
    """Appointments module client."""

    def __init__(self, client: HttpClient) -> None:
        self.client = client

    def get_appointments(
        self, limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Appointment]:
        """Get all appointments."""
        data = self.client.get(
            "/api/project-appointments", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Appointment)

    async def get_appointments_async(
        self, limit: int = 50, page: int = 1, search: Optional[str] = None
    ) -> PaginatedResponse[Appointment]:
        """Get all appointments (async)."""
        data = await self.client.get_async(
            "/api/project-appointments", limit=limit, page=page, search=search
        )
        return self._parse_paginated_response(data, Appointment)

    def get_appointment(self, appointment_id: str) -> Appointment:
        """Get an appointment by ID."""
        data = self.client.get(f"/api/project-appointments/{appointment_id}")
        return Appointment(**data)

    async def get_appointment_async(self, appointment_id: str) -> Appointment:
        """Get an appointment by ID (async)."""
        data = await self.client.get_async(f"/api/project-appointments/{appointment_id}")
        return Appointment(**data)

    def create_appointment(self, body: CreateAppointmentBody) -> Appointment:
        """Create an appointment."""
        data = self.client.post(
            "/api/project-appointments",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Appointment(**data)

    async def create_appointment_async(self, body: CreateAppointmentBody) -> Appointment:
        """Create an appointment (async)."""
        data = await self.client.post_async(
            "/api/project-appointments",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Appointment(**data)

    def update_appointment(self, appointment_id: str, body: UpdateAppointmentBody) -> Appointment:
        """Update an appointment."""
        data = self.client.put(
            f"/api/project-appointments/{appointment_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Appointment(**data)

    async def update_appointment_async(
        self, appointment_id: str, body: UpdateAppointmentBody
    ) -> Appointment:
        """Update an appointment (async)."""
        data = await self.client.put_async(
            f"/api/project-appointments/{appointment_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Appointment(**data)

    def delete_appointment(self, appointment_id: str) -> None:
        """Delete an appointment."""
        self.client.delete(f"/api/project-appointments/{appointment_id}")

    async def delete_appointment_async(self, appointment_id: str) -> None:
        """Delete an appointment (async)."""
        await self.client.delete_async(f"/api/project-appointments/{appointment_id}")

    def get_stats(self) -> AppointmentStats:
        """Get appointment statistics."""
        data = self.client.get("/api/project-appointments/stats")
        return AppointmentStats(**data)

    async def get_stats_async(self) -> AppointmentStats:
        """Get appointment statistics (async)."""
        data = await self.client.get_async("/api/project-appointments/stats")
        return AppointmentStats(**data)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
