import { HttpClient } from '../client';
import type {
  Vendor,
  CreateVendorBody,
  UpdateVendorBody,
  VendorListParams,
  VendorStats,
} from '../types/vendors';
import type { PaginationMetadata } from '../types/common';

export class VendorsModule {
  constructor(private client: HttpClient) {}

  /**
   * List vendors with pagination and filters
   */
  async listVendors(params?: VendorListParams): Promise<{
    vendors: Vendor[];
    pagination: PaginationMetadata;
  }> {
    const response = await this.client.get<{
      vendors: Vendor[];
      pagination: PaginationMetadata;
    }>('/api/project-vendors', { params });
    return response;
  }

  /**
   * Get a single vendor by ID
   */
  async getVendor(id: string): Promise<Vendor> {
    return this.client.get<Vendor>(`/vendors/${id}`);
  }

  /**
   * Create a new vendor
   */
  async createVendor(body: CreateVendorBody): Promise<Vendor> {
    return this.client.post<Vendor>('/api/project-vendors', body);
  }

  /**
   * Update a vendor
   */
  async updateVendor(id: string, body: UpdateVendorBody): Promise<Vendor> {
    return this.client.put<Vendor>(`/vendors/${id}`, body);
  }

  /**
   * Delete a vendor
   */
  async deleteVendor(id: string): Promise<void> {
    await this.client.delete(`/vendors/${id}`);
  }

  /**
   * Get vendor statistics
   */
  async getStats(): Promise<VendorStats> {
    return this.client.get<VendorStats>('/api/project-vendors/stats');
  }
}
