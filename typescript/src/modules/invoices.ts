import { HttpClient } from '../client';
import type {
  Invoice,
  CreateInvoiceBody,
  UpdateInvoiceBody,
  InvoiceListParams,
  InvoiceStats,
} from '../types/invoices';
import type { PaginationMetadata } from '../types/common';

export class InvoicesModule {
  constructor(private client: HttpClient) {}

  /**
   * List invoices with pagination and filters
   */
  async listInvoices(params?: InvoiceListParams): Promise<{
    invoices: Invoice[];
    pagination: PaginationMetadata;
  }> {
    const response = await this.client.get<{
      invoices: Invoice[];
      pagination: PaginationMetadata;
    }>('/api/project-invoices', { params });
    return response;
  }

  /**
   * Get a single invoice by ID
   */
  async getInvoice(id: string): Promise<Invoice> {
    return this.client.get<Invoice>(`/invoices/${id}`);
  }

  /**
   * Create a new invoice
   */
  async createInvoice(body: CreateInvoiceBody): Promise<Invoice> {
    return this.client.post<Invoice>('/api/project-invoices', body);
  }

  /**
   * Update an invoice
   */
  async updateInvoice(id: string, body: UpdateInvoiceBody): Promise<Invoice> {
    return this.client.put<Invoice>(`/invoices/${id}`, body);
  }

  /**
   * Delete an invoice
   */
  async deleteInvoice(id: string): Promise<void> {
    await this.client.delete(`/invoices/${id}`);
  }

  /**
   * Get invoice statistics
   */
  async getStats(): Promise<InvoiceStats> {
    return this.client.get<InvoiceStats>('/api/project-invoices/stats');
  }
}
