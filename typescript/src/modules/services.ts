import { HttpClient } from '../client';
import type {
  Service,
  CreateServiceBody,
  UpdateServiceBody,
  ServiceListParams,
  ServiceStats,
} from '../types/services';
import type { PaginationMetadata } from '../types/common';

export class ServicesModule {
  constructor(private client: HttpClient) {}

  /**
   * List services with pagination and filters
   */
  async listServices(params?: ServiceListParams): Promise<{
    services: Service[];
    pagination: PaginationMetadata;
  }> {
    const response = await this.client.get<{
      services: Service[];
      pagination: PaginationMetadata;
    }>('/api/project-services', { params });
    return response;
  }

  /**
   * Get a single service by ID
   */
  async getService(id: string): Promise<Service> {
    return this.client.get<Service>(`/services/${id}`);
  }

  /**
   * Create a new service
   */
  async createService(body: CreateServiceBody): Promise<Service> {
    return this.client.post<Service>('/api/project-services', body);
  }

  /**
   * Update a service
   */
  async updateService(id: string, body: UpdateServiceBody): Promise<Service> {
    return this.client.put<Service>(`/services/${id}`, body);
  }

  /**
   * Delete a service
   */
  async deleteService(id: string): Promise<void> {
    await this.client.delete(`/services/${id}`);
  }

  /**
   * Get service statistics
   */
  async getStats(): Promise<ServiceStats> {
    return this.client.get<ServiceStats>('/api/project-services/stats');
  }
}
