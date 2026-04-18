import { ServiceStatus, Currency, Money, DateTime, UUID } from './common';

/**
 * Service response object
 */
export interface Service {
  id: UUID;
  name: string;
  slug: string;
  description: string | null;
  shortDesc: string | null;
  category: string | null;
  price: Money | null;
  currency: Currency;
  durationMins: number | null;
  imageUrl: string | null;
  status: ServiceStatus;
  featured: boolean;
  sortOrder: number;
  metaJson: any | null;
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * Create service request body
 */
export interface CreateServiceBody {
  projectId: UUID;
  name: string;
  slug?: string;
  description?: string | null;
  shortDesc?: string | null;
  category?: string | null;
  priceCents?: number | null;
  currency?: Currency;
  durationMins?: number | null;
  imageUrl?: string | null;
  status?: ServiceStatus;
  featured?: boolean;
  sortOrder?: number;
  metaJson?: any | null;
}

/**
 * Update service request body
 */
export interface UpdateServiceBody {
  name?: string;
  slug?: string;
  description?: string | null;
  shortDesc?: string | null;
  category?: string | null;
  priceCents?: number | null;
  currency?: Currency;
  durationMins?: number | null;
  imageUrl?: string | null;
  status?: ServiceStatus;
  featured?: boolean;
  sortOrder?: number;
  metaJson?: any | null;
}

/**
 * Service list query parameters
 */
export interface ServiceListParams {
  projectId?: UUID;
  search?: string;
  category?: string;
  status?: ServiceStatus;
  featured?: boolean;
  limit?: number;
  page?: number;
}

/**
 * Service statistics response
 */
export interface ServiceStats {
  total: number;
  active: number;
  inactive: number;
  draft: number;
  featured: number;
}
