import { HttpClient } from '../client';
import type {
  Shipment,
  CreateShipmentBody,
  UpdateShipmentBody,
  ShipmentListParams,
  ShipmentStats,
} from '../types/shipments';
import type { PaginationMetadata } from '../types/common';

export class ShipmentsModule {
  constructor(private client: HttpClient) {}

  /**
   * List shipments with pagination and filters
   */
  async listShipments(params?: ShipmentListParams): Promise<{
    shipments: Shipment[];
    pagination: PaginationMetadata;
  }> {
    const response = await this.client.get<{
      shipments: Shipment[];
      pagination: PaginationMetadata;
    }>('/api/project-shipments', { params });
    return response;
  }

  /**
   * Get a single shipment by ID
   */
  async getShipment(id: string): Promise<Shipment> {
    return this.client.get<Shipment>(`/shipments/${id}`);
  }

  /**
   * Create a new shipment
   */
  async createShipment(body: CreateShipmentBody): Promise<Shipment> {
    return this.client.post<Shipment>('/api/project-shipments', body);
  }

  /**
   * Update a shipment
   */
  async updateShipment(id: string, body: UpdateShipmentBody): Promise<Shipment> {
    return this.client.put<Shipment>(`/shipments/${id}`, body);
  }

  /**
   * Delete a shipment
   */
  async deleteShipment(id: string): Promise<void> {
    await this.client.delete(`/shipments/${id}`);
  }

  /**
   * Get shipment statistics
   */
  async getStats(): Promise<ShipmentStats> {
    return this.client.get<ShipmentStats>('/api/project-shipments/stats');
  }
}
