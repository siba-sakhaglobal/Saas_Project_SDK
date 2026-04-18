import { HttpClient } from '../client';
import type {
  EndUser,
  RegisterEndUserBody,
  LoginEndUserBody,
  LoginEndUserResponse,
  UpdateEndUserProfileBody,
  ChangePasswordBody,
  RequestPasswordResetBody,
  ResetPasswordBody,
  EndUserListParams,
  EndUserStats,
} from '../types/users';
import type { PaginationMetadata } from '../types/common';

export class UsersModule {
  constructor(private client: HttpClient) {}

  /**
   * Register a new end-user account
   */
  async register(body: RegisterEndUserBody): Promise<LoginEndUserResponse> {
    return this.client.post<LoginEndUserResponse>('/api/v1/users/register', body);
  }

  /**
   * Login an end-user
   */
  async login(body: LoginEndUserBody): Promise<LoginEndUserResponse> {
    return this.client.post<LoginEndUserResponse>('/api/v1/users/login', body);
  }

  /**
   * Get current authenticated user profile
   */
  async getProfile(): Promise<EndUser> {
    return this.client.get<EndUser>('/api/v1/users/me');
  }

  /**
   * Update current user profile
   */
  async updateProfile(body: UpdateEndUserProfileBody): Promise<EndUser> {
    return this.client.put<EndUser>('/api/v1/users/me', body);
  }

  /**
   * Refresh authentication token
   */
  async refresh(): Promise<LoginEndUserResponse> {
    return this.client.post<LoginEndUserResponse>('/api/v1/users/refresh', {});
  }

  /**
   * Logout current user
   */
  async logout(): Promise<void> {
    await this.client.post('/api/v1/users/logout', {});
  }

  /**
   * Get signup fields configuration
   */
  async getSignupFields(): Promise<any> {
    return this.client.get<any>('/api/v1/users/signup-fields');
  }

  /**
   * List end-users (admin only)
   */
  async listUsers(params?: EndUserListParams): Promise<{
    users: EndUser[];
    pagination: PaginationMetadata;
  }> {
    const response = await this.client.get<{
      users: EndUser[];
      pagination: PaginationMetadata;
    }>('/api/v1/users', { params });
    return response;
  }

  /**
   * Get a single user by ID (admin only)
   */
  async getUser(id: string): Promise<EndUser> {
    return this.client.get<EndUser>(`/api/v1/users/${id}`);
  }

  /**
   * Get user statistics (admin only)
   */
  async getStats(): Promise<EndUserStats> {
    return this.client.get<EndUserStats>('/api/v1/users/stats');
  }
}
