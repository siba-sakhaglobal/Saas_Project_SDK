import { UUID, DateTime } from './common';

/**
 * Vendor response object
 */
export interface Vendor {
  id: UUID;
  name: string;
  slug: string;
  email: string;
  phone: string | null;
  company: string | null;
  address: string | null;
  description: string | null;
  logoUrl: string | null;
  status: 'active' | 'inactive' | 'suspended';
  rating: number | null;
  productCount: number;
  commissionPct: number | null;
  metaJson: any | null;
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * Create vendor request body
 */
export interface CreateVendorBody {
  projectId: UUID;
  name: string;
  slug?: string | null;
  email: string;
  phone?: string | null;
  company?: string | null;
  address?: string | null;
  description?: string | null;
  logoUrl?: string | null;
  status?: 'active' | 'inactive' | 'suspended';
  rating?: number | null;
  productCount?: number;
  commissionPct?: number | null;
  metaJson?: any | null;
}

/**
 * Update vendor request body
 */
export interface UpdateVendorBody {
  name?: string;
  slug?: string | null;
  email?: string;
  phone?: string | null;
  company?: string | null;
  address?: string | null;
  description?: string | null;
  logoUrl?: string | null;
  status?: 'active' | 'inactive' | 'suspended';
  rating?: number | null;
  productCount?: number;
  commissionPct?: number | null;
  metaJson?: any | null;
}

/**
 * Vendor list query parameters
 */
export interface VendorListParams {
  projectId?: UUID;
  search?: string;
  status?: 'active' | 'inactive' | 'suspended';
  limit?: number;
  page?: number;
}

/**
 * Vendor statistics response
 */
export interface VendorStats {
  total: number;
  active: number;
  inactive: number;
  suspended: number;
}
