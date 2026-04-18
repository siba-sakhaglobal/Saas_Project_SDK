import { DateTime, UUID } from './common';

/**
 * Banner response object
 */
export interface Banner {
  id: UUID;
  title: string;
  subtitle: string | null;
  imageUrl: string;
  mobileImageUrl: string | null;
  linkUrl: string | null;
  linkTarget: '_self' | '_blank';
  placement: 'hero' | 'sidebar' | 'footer' | 'popup' | 'other';
  status: 'active' | 'inactive' | 'scheduled' | 'expired';
  sortOrder: number;
  bgColor: string | null;
  textColor: string | null;
  startDate: DateTime | null;
  endDate: DateTime | null;
  clickCount: number;
  metaJson: any | null;
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * Create banner request body
 */
export interface CreateBannerBody {
  projectId: UUID;
  title: string;
  subtitle?: string | null;
  imageUrl: string;
  mobileImageUrl?: string | null;
  linkUrl?: string | null;
  linkTarget?: '_self' | '_blank';
  placement?: 'hero' | 'sidebar' | 'footer' | 'popup' | 'other';
  status?: 'active' | 'inactive' | 'scheduled' | 'expired';
  sortOrder?: number;
  bgColor?: string | null;
  textColor?: string | null;
  startDate?: DateTime | null;
  endDate?: DateTime | null;
  metaJson?: any | null;
}

/**
 * Update banner request body
 */
export interface UpdateBannerBody {
  title?: string;
  subtitle?: string | null;
  imageUrl?: string;
  mobileImageUrl?: string | null;
  linkUrl?: string | null;
  linkTarget?: '_self' | '_blank';
  placement?: 'hero' | 'sidebar' | 'footer' | 'popup' | 'other';
  status?: 'active' | 'inactive' | 'scheduled' | 'expired';
  sortOrder?: number;
  bgColor?: string | null;
  textColor?: string | null;
  startDate?: DateTime | null;
  endDate?: DateTime | null;
  metaJson?: any | null;
}

/**
 * Banner list query parameters
 */
export interface BannerListParams {
  projectId?: UUID;
  search?: string;
  status?: 'active' | 'inactive' | 'scheduled' | 'expired';
  placement?: 'hero' | 'sidebar' | 'footer' | 'popup' | 'other';
  limit?: number;
  page?: number;
}

/**
 * Banner statistics response
 */
export interface BannerStats {
  total: number;
  active: number;
  inactive: number;
  scheduled: number;
  expired: number;
}
