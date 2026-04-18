"""Shipments module models."""

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class Shipment(BaseModel):
    """Shipment."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    project_id: Optional[str] = Field(None, alias="project_id")
    order_id: str = Field(alias="order_id")
    tracking_number: Optional[str] = Field(None, alias="tracking_number")
    carrier: Optional[str] = None
    status: str  # pending|shipped|in-transit|delivered|returned|cancelled
    shipped_date: Optional[datetime] = Field(None, alias="shipped_date")
    delivery_date: Optional[datetime] = Field(None, alias="delivery_date")
    estimated_delivery_date: Optional[datetime] = Field(None, alias="estimated_delivery_date")
    from_address: Optional[str] = Field(None, alias="from_address")
    to_address: Optional[str] = Field(None, alias="to_address")
    weight_kg: Optional[float] = Field(None, alias="weight_kg")
    cost: float = Field(default=0.0)
    notes: Optional[str] = None
    created_at: datetime = Field(alias="created_at")
    updated_at: datetime = Field(alias="updated_at")


class CreateShipmentBody(BaseModel):
    """Create shipment request."""

    model_config = ConfigDict(populate_by_name=True)

    order_id: str = Field(alias="orderId")
    tracking_number: Optional[str] = Field(None, alias="trackingNumber")
    carrier: Optional[str] = None
    status: str = "pending"
    shipped_date: Optional[datetime] = Field(None, alias="shippedDate")
    estimated_delivery_date: Optional[datetime] = Field(None, alias="estimatedDeliveryDate")
    from_address: Optional[str] = Field(None, alias="fromAddress")
    to_address: Optional[str] = Field(None, alias="toAddress")
    weight_kg: Optional[float] = Field(None, alias="weightKg")
    cost: Optional[float] = None
    notes: Optional[str] = None


class UpdateShipmentBody(BaseModel):
    """Update shipment request."""

    model_config = ConfigDict(populate_by_name=True)

    tracking_number: Optional[str] = Field(None, alias="trackingNumber")
    carrier: Optional[str] = None
    status: Optional[str] = None
    shipped_date: Optional[datetime] = Field(None, alias="shippedDate")
    delivery_date: Optional[datetime] = Field(None, alias="deliveryDate")
    estimated_delivery_date: Optional[datetime] = Field(None, alias="estimatedDeliveryDate")
    from_address: Optional[str] = Field(None, alias="fromAddress")
    to_address: Optional[str] = Field(None, alias="toAddress")
    weight_kg: Optional[float] = Field(None, alias="weightKg")
    cost: Optional[float] = None
    notes: Optional[str] = None


class ShipmentStats(BaseModel):
    """Shipment statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total_shipments: int = Field(alias="totalShipments")
    pending_shipments: int = Field(alias="pendingShipments")
    shipped_shipments: int = Field(alias="shippedShipments")
    delivered_shipments: int = Field(alias="deliveredShipments")
    returned_shipments: int = Field(alias="returnedShipments")
    total_cost: float = Field(alias="totalCost")
    average_delivery_time: float = Field(alias="averageDeliveryTime")
