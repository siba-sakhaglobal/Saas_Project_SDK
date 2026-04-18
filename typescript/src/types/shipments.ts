import { Currency, Money, DateTime, UUID } from './common';

/**
 * Shipment response object
 */
export interface Shipment {
  id: UUID;
  orderId: UUID | null;
  trackingNumber: string;
  carrier: string;
  status: 'pending' | 'picked_up' | 'in_transit' | 'out_for_delivery' | 'delivered' | 'returned' | 'failed';
  shippingAddress: any | null;
  weightGrams: number | null;
  cost: Money | null;
  currency: Currency;
  shippedAt: DateTime | null;
  deliveredAt: DateTime | null;
  estimatedDelivery: DateTime | null;
  notes: string | null;
  metaJson: any | null;
  createdAt: DateTime;
  updatedAt: DateTime;
  order?: {
    id: UUID;
    orderNumber: string;
    customerName: string;
  } | null;
}

/**
 * Create shipment request body
 */
export interface CreateShipmentBody {
  orderId?: UUID | null;
  trackingNumber: string;
  carrier: string;
  status?: 'pending' | 'picked_up' | 'in_transit' | 'out_for_delivery' | 'delivered' | 'returned' | 'failed';
  shippingAddress?: any | null;
  weightGrams?: number | null;
  costCents?: number | null;
  currency?: Currency;
  shippedAt?: DateTime | null;
  deliveredAt?: DateTime | null;
  estimatedDelivery?: DateTime | null;
  notes?: string | null;
  metaJson?: any | null;
}

/**
 * Update shipment request body
 */
export interface UpdateShipmentBody {
  trackingNumber?: string;
  carrier?: string;
  status?: 'pending' | 'picked_up' | 'in_transit' | 'out_for_delivery' | 'delivered' | 'returned' | 'failed';
  shippingAddress?: any | null;
  weightGrams?: number | null;
  costCents?: number | null;
  shippedAt?: DateTime | null;
  deliveredAt?: DateTime | null;
  estimatedDelivery?: DateTime | null;
  notes?: string | null;
  metaJson?: any | null;
}

/**
 * Shipment list query parameters
 */
export interface ShipmentListParams {
  page?: number;
  limit?: number;
  search?: string;
  status?: 'pending' | 'picked_up' | 'in_transit' | 'out_for_delivery' | 'delivered' | 'returned' | 'failed';
  carrier?: string;
  orderId?: UUID;
}

/**
 * Shipment statistics response
 */
export interface ShipmentStats {
  total: number;
  pending: number;
  picked_up: number;
  in_transit: number;
  out_for_delivery: number;
  delivered: number;
  returned: number;
  failed: number;
}
