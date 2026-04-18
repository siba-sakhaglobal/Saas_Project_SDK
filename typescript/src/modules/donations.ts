import { HttpClient } from '../client';
import type {
  DonationCampaign,
  Donation,
  CreateCampaignBody,
  UpdateCampaignBody,
  CampaignListParams,
  DonationListParams,
  DonationStats,
} from '../types/donations';
import type { PaginationMetadata } from '../types/common';

export class DonationsModule {
  constructor(private client: HttpClient) {}

  /**
   * List donation campaigns with pagination and filters
   */
  async listCampaigns(params?: CampaignListParams): Promise<{
    campaigns: DonationCampaign[];
    pagination: PaginationMetadata;
  }> {
    const response = await this.client.get<{
      campaigns: DonationCampaign[];
      pagination: PaginationMetadata;
    }>('/api/donations/campaigns', { params });
    return response;
  }

  /**
   * Get a single donation campaign by ID
   */
  async getCampaign(id: string): Promise<DonationCampaign> {
    return this.client.get<DonationCampaign>(`/api/donations/campaigns/${id}`);
  }

  /**
   * Create a new donation campaign
   */
  async createCampaign(body: CreateCampaignBody): Promise<DonationCampaign> {
    return this.client.post<DonationCampaign>('/api/donations/campaigns', body);
  }

  /**
   * Update a donation campaign
   */
  async updateCampaign(
    id: string,
    body: UpdateCampaignBody
  ): Promise<DonationCampaign> {
    return this.client.put<DonationCampaign>(`/api/donations/campaigns/${id}`, body);
  }

  /**
   * Delete a donation campaign
   */
  async deleteCampaign(id: string): Promise<void> {
    await this.client.delete(`/api/donations/campaigns/${id}`);
  }

  /**
   * List donations with pagination and filters
   */
  async listDonations(params?: DonationListParams): Promise<{
    donations: Donation[];
    pagination: PaginationMetadata;
  }> {
    const response = await this.client.get<{
      donations: Donation[];
      pagination: PaginationMetadata;
    }>('/api/donations/donations', { params });
    return response;
  }

  /**
   * Get a single donation by ID
   */
  async getDonation(id: string): Promise<Donation> {
    return this.client.get<Donation>(`/api/donations/donations/${id}`);
  }

  /**
   * Get donation statistics
   */
  async getStats(): Promise<DonationStats> {
    return this.client.get<DonationStats>('/api/donations/stats');
  }
}
