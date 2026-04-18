import { HttpClient } from '../client';
import type {
  Order,
  CreateOrderBody,
  UpdateOrderBody,
  OrderListParams,
  OrderStats,
} from '../types/orders';
import type { PaginationMetadata } from '../types/common';

export class OrdersModule {
  constructor(private client: HttpClient) {}

  /**
   * List orders with pagination and filters
   */
  async listOrders(params?: OrderListParams): Promise<{
    orders: Order[];
    pagination: PaginationMetadata;
  }> {
    const response = await this.client.get<{
      orders: Order[];
      pagination: PaginationMetadata;
    }>('/api/project-orders', { params });
    return response;
  }

  /**
   * Get a single order by ID
   */
  async getOrder(id: string): Promise<Order> {
    return this.client.get<Order>(`/orders/${id}`);
  }

  /**
   * Create a new order
   */
  async createOrder(body: CreateOrderBody): Promise<Order> {
    return this.client.post<Order>('/api/project-orders', body);
  }

  /**
   * Update an order
   */
  async updateOrder(id: string, body: UpdateOrderBody): Promise<Order> {
    return this.client.put<Order>(`/orders/${id}`, body);
  }

  /**
   * Delete an order
   */
  async deleteOrder(id: string): Promise<void> {
    await this.client.delete(`/orders/${id}`);
  }

  /**
   * Get order statistics
   */
  async getStats(): Promise<OrderStats> {
    return this.client.get<OrderStats>('/api/project-orders/stats');
  }
}
