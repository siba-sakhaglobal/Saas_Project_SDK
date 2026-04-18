import { TransactionType, TransactionStatus, Currency, Money, DateTime, UUID } from './common';

/**
 * Payment method enum
 */
export type PaymentMethod = 'card' | 'bank_transfer' | 'cash' | 'check' | 'other';

/**
 * Transaction response object
 */
export interface Transaction {
  id: UUID;
  orderId: UUID | null;
  orderNumber: string | null;
  invoiceId: UUID | null;
  invoiceNumber: string | null;
  transactionRef: string | null;
  type: TransactionType;
  amount: Money;
  currency: Currency;
  status: TransactionStatus;
  paymentMethod: PaymentMethod | null;
  paymentGateway: string | null;
  gatewayRef: string | null;
  customerName: string;
  customerEmail: string;
  description: string | null;
  metaJson: any | null;
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * Create transaction request body
 */
export interface CreateTransactionBody {
  projectId: UUID;
  orderId?: UUID | null;
  invoiceId?: UUID | null;
  transactionRef?: string | null;
  type: TransactionType;
  amountCents: number;
  currency?: Currency;
  status?: TransactionStatus;
  paymentMethod?: PaymentMethod | null;
  paymentGateway?: string | null;
  gatewayRef?: string | null;
  customerName: string;
  customerEmail: string;
  description?: string | null;
  metaJson?: any | null;
}

/**
 * Update transaction request body
 */
export interface UpdateTransactionBody {
  orderId?: UUID | null;
  invoiceId?: UUID | null;
  transactionRef?: string | null;
  type?: TransactionType;
  amountCents?: number;
  currency?: Currency;
  status?: TransactionStatus;
  paymentMethod?: PaymentMethod | null;
  paymentGateway?: string | null;
  gatewayRef?: string | null;
  customerName?: string;
  customerEmail?: string;
  description?: string | null;
  metaJson?: any | null;
}

/**
 * Transaction list query parameters
 */
export interface TransactionListParams {
  projectId?: UUID;
  search?: string;
  status?: TransactionStatus;
  type?: TransactionType;
  paymentMethod?: PaymentMethod;
  orderId?: UUID;
  invoiceId?: UUID;
  from?: DateTime;
  to?: DateTime;
  limit?: number;
  page?: number;
}

/**
 * Transaction statistics response
 */
export interface TransactionStats {
  total: number;
  pending: number;
  completed: number;
  failed: number;
  cancelled: number;
  totalRevenue: Money;
  totalRefunds: Money;
}
