"""Orders module models."""

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class Order(BaseModel):
    """Order."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    project_id: Optional[str] = Field(None, alias="project_id")
    customer_name: Optional[str] = Field(None, alias="customer_name")
    customer_email: Optional[str] = Field(None, alias="customer_email")
    customer_phone: Optional[str] = Field(None, alias="customer_phone")
    order_number: Optional[str] = Field(None, alias="order_number")
    total_amount: float = Field(alias="total_amount")
    discount: float = Field(default=0.0)
    tax: float = Field(default=0.0)
    subtotal: float
    payment_status: str  # pending|completed|failed|refunded
    fulfillment_status: str  # pending|processing|shipped|delivered|cancelled
    shipping_address: Optional[str] = Field(None, alias="shipping_address")
    billing_address: Optional[str] = Field(None, alias="billing_address")
    items_count: int = Field(default=0, alias="items_count")
    notes: Optional[str] = None
    created_at: datetime = Field(alias="created_at")
    updated_at: datetime = Field(alias="updated_at")


class OrderItem(BaseModel):
    """Order item."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    order_id: str = Field(alias="order_id")
    product_id: Optional[str] = Field(None, alias="product_id")
    product_name: Optional[str] = Field(None, alias="product_name")
    quantity: int
    unit_price: float = Field(alias="unit_price")
    total_price: float = Field(alias="total_price")
    created_at: datetime = Field(alias="created_at")


class CreateOrderBody(BaseModel):
    """Create order request."""

    model_config = ConfigDict(populate_by_name=True)

    customer_name: str = Field(alias="customerName")
    customer_email: str = Field(alias="customerEmail")
    customer_phone: Optional[str] = Field(None, alias="customerPhone")
    total_amount: float = Field(alias="totalAmount")
    discount: Optional[float] = None
    tax: Optional[float] = None
    subtotal: float
    payment_status: str = "pending"
    fulfillment_status: str = "pending"
    shipping_address: Optional[str] = Field(None, alias="shippingAddress")
    billing_address: Optional[str] = Field(None, alias="billingAddress")
    notes: Optional[str] = None


class UpdateOrderBody(BaseModel):
    """Update order request."""

    model_config = ConfigDict(populate_by_name=True)

    customer_name: Optional[str] = Field(None, alias="customerName")
    customer_email: Optional[str] = Field(None, alias="customerEmail")
    customer_phone: Optional[str] = Field(None, alias="customerPhone")
    total_amount: Optional[float] = Field(None, alias="totalAmount")
    discount: Optional[float] = None
    tax: Optional[float] = None
    subtotal: Optional[float] = None
    payment_status: Optional[str] = None
    fulfillment_status: Optional[str] = None
    shipping_address: Optional[str] = Field(None, alias="shippingAddress")
    billing_address: Optional[str] = Field(None, alias="billingAddress")
    notes: Optional[str] = None


class OrderStats(BaseModel):
    """Order statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total_orders: int = Field(alias="totalOrders")
    pending_orders: int = Field(alias="pendingOrders")
    completed_orders: int = Field(alias="completedOrders")
    failed_orders: int = Field(alias="failedOrders")
    total_revenue: float = Field(alias="totalRevenue")
    average_order_value: float = Field(alias="averageOrderValue")
    total_items_sold: int = Field(alias="totalItemsSold")
