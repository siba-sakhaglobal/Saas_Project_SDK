/**
 * Common types used across all SDK modules
 */

/**
 * Standard API response envelope
 */
export interface ApiResponse<T> {
  success: boolean;
  data: T | null;
  error: string | Record<string, string[]> | null;
  metadata?: PaginationMetadata;
}

/**
 * Pagination metadata included in list responses
 */
export interface PaginationMetadata {
  total: number;
  page: number;
  limit: number;
}

/**
 * Standard list query parameters
 */
export interface ListParams {
  page?: number;
  limit?: number;
  search?: string;
}

/**
 * Date range filter parameters
 */
export interface DateRangeParams {
  from?: string;
  to?: string;
}

/**
 * Error response structure
 */
export interface ErrorResponse {
  code?: string;
  message: string;
  details?: Record<string, string[]>;
}

/**
 * Currency codes supported by the CMS
 */
export type Currency = 'USD' | 'EUR' | 'GBP' | 'INR';

/**
 * Status values for various entities
 */
export type PostStatus = 'draft' | 'published' | 'archived';
export type EventStatus = 'upcoming' | 'ongoing' | 'completed' | 'cancelled';
export type DonationStatus = 'active' | 'paused' | 'completed';
export type OrderStatus = 'processing' | 'pending' | 'confirmed' | 'delivered' | 'cancelled' | 'refunded';
export type InvoiceStatus = 'draft' | 'sent' | 'paid' | 'overdue' | 'cancelled' | 'refunded';
export type TransactionType = 'payment' | 'refund' | 'adjustment';
export type TransactionStatus = 'pending' | 'completed' | 'failed' | 'cancelled';
export type ServiceStatus = 'active' | 'inactive' | 'draft';
export type AppointmentStatus = 'scheduled' | 'confirmed' | 'completed' | 'cancelled';
export type VendorStatus = 'active' | 'inactive' | 'suspended';
export type ProductStatus = 'draft' | 'active' | 'inactive' | 'archived';
export type ShipmentStatus = 'pending' | 'picked_up' | 'in_transit' | 'out_for_delivery' | 'delivered' | 'returned' | 'failed';
export type BannerStatus = 'active' | 'inactive' | 'scheduled' | 'expired';
export type BannerPlacement = 'hero' | 'sidebar' | 'footer' | 'popup' | 'other';

/**
 * Author object used in responses
 */
export interface Author {
  id: string | null;
  name: string;
  avatar: string | null;
  role: string;
}

/**
 * Category object used in responses
 */
export interface CategoryInfo {
  name: string;
  color?: string;
}

/**
 * Monetary amount - stored as cents in DB, converted to dollars in API
 */
export type Money = number; // In dollars (e.g., 99.99)

/**
 * UUID type
 */
export type UUID = string & { readonly __brand: 'UUID' };

/**
 * ISO8601 datetime string
 */
export type DateTime = string & { readonly __brand: 'DateTime' };
