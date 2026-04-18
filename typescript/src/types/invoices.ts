import { InvoiceStatus, Currency, Money, DateTime, UUID } from './common';

/**
 * Invoice response object
 */
export interface Invoice {
  id: UUID;
  invoiceNumber: string;
  orderId: UUID | null;
  orderNumber: string | null;
  customerName: string;
  customerEmail: string;
  status: InvoiceStatus;
  subtotal: Money | null;
  tax: Money | null;
  discount: Money | null;
  total: Money | null;
  currency: Currency;
  itemsJson: any | null;
  dueDate: DateTime | null;
  paidAt: DateTime | null;
  notes: string | null;
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * Create invoice request body
 */
export interface CreateInvoiceBody {
  projectId: UUID;
  orderId?: UUID | null;
  customerName: string;
  customerEmail: string;
  status?: InvoiceStatus;
  subtotalCents?: number | null;
  taxCents?: number | null;
  discountCents?: number | null;
  totalCents?: number | null;
  currency?: Currency;
  itemsJson?: any | null;
  dueDate?: DateTime | null;
  paidAt?: DateTime | null;
  notes?: string | null;
}

/**
 * Update invoice request body
 */
export interface UpdateInvoiceBody {
  orderId?: UUID | null;
  customerName?: string;
  customerEmail?: string;
  status?: InvoiceStatus;
  subtotalCents?: number | null;
  taxCents?: number | null;
  discountCents?: number | null;
  totalCents?: number | null;
  currency?: Currency;
  itemsJson?: any | null;
  dueDate?: DateTime | null;
  paidAt?: DateTime | null;
  notes?: string | null;
}

/**
 * Invoice list query parameters
 */
export interface InvoiceListParams {
  projectId?: UUID;
  search?: string;
  status?: InvoiceStatus;
  orderId?: UUID;
  from?: DateTime;
  to?: DateTime;
  limit?: number;
  page?: number;
}

/**
 * Invoice statistics response
 */
export interface InvoiceStats {
  total: number;
  draft: number;
  sent: number;
  paid: number;
  overdue: number;
  cancelled: number;
  totalPaid: Money;
  overdueCount: number;
}
