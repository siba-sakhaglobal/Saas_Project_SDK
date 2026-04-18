"""Appointments module models."""

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class Appointment(BaseModel):
    """Appointment."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    project_id: Optional[str] = Field(None, alias="project_id")
    service_id: str = Field(alias="service_id")
    customer_name: str = Field(alias="customer_name")
    customer_email: str = Field(alias="customer_email")
    customer_phone: Optional[str] = Field(None, alias="customer_phone")
    appointment_date: datetime = Field(alias="appointment_date")
    appointment_time: str = Field(alias="appointment_time")
    duration_minutes: int = Field(alias="duration_minutes")
    status: str  # scheduled|confirmed|completed|cancelled|no-show
    notes: Optional[str] = None
    location: Optional[str] = None
    created_at: datetime = Field(alias="created_at")
    updated_at: datetime = Field(alias="updated_at")


class CreateAppointmentBody(BaseModel):
    """Create appointment request."""

    model_config = ConfigDict(populate_by_name=True)

    service_id: str = Field(alias="serviceId")
    customer_name: str = Field(alias="customerName")
    customer_email: str = Field(alias="customerEmail")
    customer_phone: Optional[str] = Field(None, alias="customerPhone")
    appointment_date: datetime = Field(alias="appointmentDate")
    appointment_time: str = Field(alias="appointmentTime")
    duration_minutes: int = Field(alias="durationMinutes")
    status: str = "scheduled"
    notes: Optional[str] = None
    location: Optional[str] = None


class UpdateAppointmentBody(BaseModel):
    """Update appointment request."""

    model_config = ConfigDict(populate_by_name=True)

    service_id: Optional[str] = Field(None, alias="serviceId")
    customer_name: Optional[str] = Field(None, alias="customerName")
    customer_email: Optional[str] = Field(None, alias="customerEmail")
    customer_phone: Optional[str] = Field(None, alias="customerPhone")
    appointment_date: Optional[datetime] = Field(None, alias="appointmentDate")
    appointment_time: Optional[str] = Field(None, alias="appointmentTime")
    duration_minutes: Optional[int] = Field(None, alias="durationMinutes")
    status: Optional[str] = None
    notes: Optional[str] = None
    location: Optional[str] = None


class AppointmentStats(BaseModel):
    """Appointment statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total_appointments: int = Field(alias="totalAppointments")
    scheduled_appointments: int = Field(alias="scheduledAppointments")
    completed_appointments: int = Field(alias="completedAppointments")
    cancelled_appointments: int = Field(alias="cancelledAppointments")
    no_show_appointments: int = Field(alias="noShowAppointments")
    total_revenue: float = Field(alias="totalRevenue")
