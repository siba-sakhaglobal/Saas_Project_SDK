"""Invoices module models."""

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class Invoice(BaseModel):
    """Invoice."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    project_id: Optional[str] = Field(None, alias="project_id")
    invoice_number: Optional[str] = Field(None, alias="invoice_number")
    order_id: Optional[str] = Field(None, alias="order_id")
    customer_name: Optional[str] = Field(None, alias="customer_name")
    customer_email: Optional[str] = Field(None, alias="customer_email")
    subtotal: float
    tax: float = Field(default=0.0)
    total: float
    status: str  # draft|sent|viewed|paid|overdue|cancelled
    due_date: Optional[datetime] = Field(None, alias="due_date")
    issued_at: Optional[datetime] = Field(None, alias="issued_at")
    paid_at: Optional[datetime] = Field(None, alias="paid_at")
    payment_method: Optional[str] = Field(None, alias="payment_method")
    notes: Optional[str] = None
    created_at: datetime = Field(alias="created_at")
    updated_at: datetime = Field(alias="updated_at")


class InvoiceItem(BaseModel):
    """Invoice line item."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    invoice_id: str = Field(alias="invoice_id")
    description: str
    quantity: int
    unit_price: float = Field(alias="unit_price")
    total_price: float = Field(alias="total_price")


class CreateInvoiceBody(BaseModel):
    """Create invoice request."""

    model_config = ConfigDict(populate_by_name=True)

    invoice_number: Optional[str] = Field(None, alias="invoiceNumber")
    order_id: Optional[str] = Field(None, alias="orderId")
    customer_name: str = Field(alias="customerName")
    customer_email: str = Field(alias="customerEmail")
    subtotal: float
    tax: Optional[float] = None
    total: float
    status: str = "draft"
    due_date: Optional[datetime] = Field(None, alias="dueDate")
    issued_at: Optional[datetime] = Field(None, alias="issuedAt")
    payment_method: Optional[str] = Field(None, alias="paymentMethod")
    notes: Optional[str] = None


class UpdateInvoiceBody(BaseModel):
    """Update invoice request."""

    model_config = ConfigDict(populate_by_name=True)

    invoice_number: Optional[str] = Field(None, alias="invoiceNumber")
    customer_name: Optional[str] = Field(None, alias="customerName")
    customer_email: Optional[str] = Field(None, alias="customerEmail")
    subtotal: Optional[float] = None
    tax: Optional[float] = None
    total: Optional[float] = None
    status: Optional[str] = None
    due_date: Optional[datetime] = Field(None, alias="dueDate")
    issued_at: Optional[datetime] = Field(None, alias="issuedAt")
    paid_at: Optional[datetime] = Field(None, alias="paidAt")
    payment_method: Optional[str] = Field(None, alias="paymentMethod")
    notes: Optional[str] = None


class InvoiceStats(BaseModel):
    """Invoice statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total_invoices: int = Field(alias="totalInvoices")
    paid_invoices: int = Field(alias="paidInvoices")
    pending_invoices: int = Field(alias="pendingInvoices")
    overdue_invoices: int = Field(alias="overdueInvoices")
    total_amount: float = Field(alias="totalAmount")
    paid_amount: float = Field(alias="paidAmount")
    pending_amount: float = Field(alias="pendingAmount")
