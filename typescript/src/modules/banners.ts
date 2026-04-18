import { HttpClient } from '../client';
import type {
  Banner,
  CreateBannerBody,
  UpdateBannerBody,
  BannerListParams,
  BannerStats,
} from '../types/banners';
import type { PaginationMetadata } from '../types/common';

export class BannersModule {
  constructor(private client: HttpClient) {}

  /**
   * List banners with pagination and filters
   */
  async listBanners(params?: BannerListParams): Promise<{
    banners: Banner[];
    pagination: PaginationMetadata;
  }> {
    const response = await this.client.get<{
      banners: Banner[];
      pagination: PaginationMetadata;
    }>('/api/project-banners', { params });
    return response;
  }

  /**
   * Get a single banner by ID
   */
  async getBanner(id: string): Promise<Banner> {
    return this.client.get<Banner>(`/banners/${id}`);
  }

  /**
   * Create a new banner
   */
  async createBanner(body: CreateBannerBody): Promise<Banner> {
    return this.client.post<Banner>('/api/project-banners', body);
  }

  /**
   * Update a banner
   */
  async updateBanner(id: string, body: UpdateBannerBody): Promise<Banner> {
    return this.client.put<Banner>(`/banners/${id}`, body);
  }

  /**
   * Delete a banner
   */
  async deleteBanner(id: string): Promise<void> {
    await this.client.delete(`/banners/${id}`);
  }

  /**
   * Get banner statistics
   */
  async getStats(): Promise<BannerStats> {
    return this.client.get<BannerStats>('/api/project-banners/stats');
  }

  /**
   * Reorder banners by sort order
   */
  async reorderBanner(id: string, sortOrder: number): Promise<Banner> {
    return this.client.put<Banner>(`/banners/${id}`, { sortOrder });
  }
}
