import { OrderStatus, Currency, Money, DateTime, UUID } from './common';

/**
 * Order response object
 */
export interface Order {
  id: UUID;
  orderNumber: string;
  customerName: string;
  customerEmail: string;
  customerPhone: string | null;
  status: OrderStatus;
  subtotal: Money | null;
  tax: Money | null;
  shipping: Money | null;
  discount: Money | null;
  total: Money | null;
  currency: Currency;
  itemsJson: any | null;
  shippingAddress: any | null;
  billingAddress: any | null;
  notes: string | null;
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * Create order request body
 */
export interface CreateOrderBody {
  projectId: UUID;
  customerName: string;
  customerEmail: string;
  customerPhone?: string | null;
  status?: OrderStatus;
  subtotalCents?: number | null;
  taxCents?: number | null;
  shippingCents?: number | null;
  discountCents?: number | null;
  totalCents?: number | null;
  currency?: Currency;
  itemsJson?: any | null;
  shippingAddress?: any | null;
  billingAddress?: any | null;
  notes?: string | null;
}

/**
 * Update order request body
 */
export interface UpdateOrderBody {
  customerName?: string;
  customerEmail?: string;
  customerPhone?: string | null;
  status?: OrderStatus;
  subtotalCents?: number | null;
  taxCents?: number | null;
  shippingCents?: number | null;
  discountCents?: number | null;
  totalCents?: number | null;
  currency?: Currency;
  itemsJson?: any | null;
  shippingAddress?: any | null;
  billingAddress?: any | null;
  notes?: string | null;
}

/**
 * Order list query parameters
 */
export interface OrderListParams {
  projectId?: UUID;
  search?: string;
  status?: OrderStatus;
  from?: DateTime;
  to?: DateTime;
  limit?: number;
  page?: number;
}

/**
 * Order statistics response
 */
export interface OrderStats {
  total: number;
  processing: number;
  pending: number;
  confirmed: number;
  delivered: number;
  cancelled: number;
  refunded: number;
  totalRevenue: Money;
}
