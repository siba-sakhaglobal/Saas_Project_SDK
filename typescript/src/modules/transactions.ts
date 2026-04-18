import { HttpClient } from '../client';
import type {
  Transaction,
  CreateTransactionBody,
  UpdateTransactionBody,
  TransactionListParams,
  TransactionStats,
} from '../types/transactions';
import type { PaginationMetadata } from '../types/common';

export class TransactionsModule {
  constructor(private client: HttpClient) {}

  /**
   * List transactions with pagination and filters
   */
  async listTransactions(params?: TransactionListParams): Promise<{
    transactions: Transaction[];
    pagination: PaginationMetadata;
  }> {
    const response = await this.client.get<{
      transactions: Transaction[];
      pagination: PaginationMetadata;
    }>('/api/project-transactions', { params });
    return response;
  }

  /**
   * Get a single transaction by ID
   */
  async getTransaction(id: string): Promise<Transaction> {
    return this.client.get<Transaction>(`/transactions/${id}`);
  }

  /**
   * Create a new transaction
   */
  async createTransaction(body: CreateTransactionBody): Promise<Transaction> {
    return this.client.post<Transaction>('/api/project-transactions', body);
  }

  /**
   * Update a transaction
   */
  async updateTransaction(
    id: string,
    body: UpdateTransactionBody
  ): Promise<Transaction> {
    return this.client.put<Transaction>(`/transactions/${id}`, body);
  }

  /**
   * Delete a transaction
   */
  async deleteTransaction(id: string): Promise<void> {
    await this.client.delete(`/transactions/${id}`);
  }

  /**
   * Get transaction statistics
   */
  async getStats(): Promise<TransactionStats> {
    return this.client.get<TransactionStats>('/api/project-transactions/stats');
  }
}
