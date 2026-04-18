"""Transactions module models."""

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class Transaction(BaseModel):
    """Transaction."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    project_id: Optional[str] = Field(None, alias="project_id")
    transaction_id: Optional[str] = Field(None, alias="transaction_id")
    order_id: Optional[str] = Field(None, alias="order_id")
    invoice_id: Optional[str] = Field(None, alias="invoice_id")
    amount: float
    type: str  # payment|refund|adjustment
    status: str  # pending|completed|failed|cancelled
    payment_method: Optional[str] = Field(None, alias="payment_method")
    payment_gateway: Optional[str] = Field(None, alias="payment_gateway")
    gateway_transaction_id: Optional[str] = Field(None, alias="gateway_transaction_id")
    description: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime = Field(alias="created_at")
    updated_at: datetime = Field(alias="updated_at")


class CreateTransactionBody(BaseModel):
    """Create transaction request."""

    model_config = ConfigDict(populate_by_name=True)

    transaction_id: Optional[str] = Field(None, alias="transactionId")
    order_id: Optional[str] = Field(None, alias="orderId")
    invoice_id: Optional[str] = Field(None, alias="invoiceId")
    amount: float
    type: str = "payment"
    status: str = "pending"
    payment_method: Optional[str] = Field(None, alias="paymentMethod")
    payment_gateway: Optional[str] = Field(None, alias="paymentGateway")
    gateway_transaction_id: Optional[str] = Field(None, alias="gatewayTransactionId")
    description: Optional[str] = None
    notes: Optional[str] = None


class UpdateTransactionBody(BaseModel):
    """Update transaction request."""

    model_config = ConfigDict(populate_by_name=True)

    status: Optional[str] = None
    amount: Optional[float] = None
    payment_method: Optional[str] = Field(None, alias="paymentMethod")
    payment_gateway: Optional[str] = Field(None, alias="paymentGateway")
    gateway_transaction_id: Optional[str] = Field(None, alias="gatewayTransactionId")
    description: Optional[str] = None
    notes: Optional[str] = None


class TransactionStats(BaseModel):
    """Transaction statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total_transactions: int = Field(alias="totalTransactions")
    successful_transactions: int = Field(alias="successfulTransactions")
    failed_transactions: int = Field(alias="failedTransactions")
    pending_transactions: int = Field(alias="pendingTransactions")
    total_amount: float = Field(alias="totalAmount")
    successful_amount: float = Field(alias="successfulAmount")
    refunded_amount: float = Field(alias="refundedAmount")
