/**
 * HTTP client for Sakha CMS SDK
 * Handles authentication, error handling, and auto-retry
 */

import { ApiResponse } from './types/common';

export interface ClientConfig {
  apiKey: string;
  apiSecret?: string;
  baseUrl?: string;
  timeout?: number;
}

export class HttpClient {
  private apiKey: string;
  private apiSecret?: string;
  private baseUrl: string;
  private timeout: number;
  private endUserToken?: string;

  constructor(config: ClientConfig) {
    this.apiKey = config.apiKey;
    this.apiSecret = config.apiSecret;
    this.baseUrl = config.baseUrl || 'http://localhost:3000';
    this.timeout = config.timeout || 30000;
  }

  /**
   * Set end-user JWT token for authenticated requests
   */
  setEndUserToken(token: string): void {
    this.endUserToken = token;
  }

  /**
   * Clear end-user token
   */
  clearEndUserToken(): void {
    this.endUserToken = undefined;
  }

  /**
   * Build Authorization header
   */
  private getAuthHeader(): string {
    if (this.endUserToken) {
      // For end-user requests: just the JWT
      return `Bearer ${this.endUserToken}`;
    }
    // For admin requests: API key and secret
    if (this.apiSecret) {
      return `Bearer ${this.apiKey}:${this.apiSecret}`;
    }
    // For end-user API key only (when calling end-user endpoints)
    return `Bearer ${this.apiKey}`;
  }

  /**
   * Make an HTTP request
   */
  async request<T>(
    method: 'GET' | 'POST' | 'PUT' | 'DELETE',
    path: string,
    options?: {
      body?: Record<string, any>;
      query?: Record<string, any>;
      headers?: Record<string, string>;
      projectId?: string;
    }
  ): Promise<T> {
    const url = this.buildUrl(path, options?.query);
    const headers = this.buildHeaders(options?.headers, options?.projectId);
    const body = options?.body ? JSON.stringify(options.body) : undefined;

    try {
      const response = await this.fetchWithTimeout(url, {
        method,
        headers,
        body,
      });

      return await this.handleResponse<T>(response);
    } catch (error) {
      this.handleError(error);
    }
  }

  /**
   * GET request
   */
  async get<T>(
    path: string,
    options?: {
      query?: Record<string, any>;
      headers?: Record<string, string>;
      projectId?: string;
    }
  ): Promise<T> {
    return this.request<T>('GET', path, options);
  }

  /**
   * POST request
   */
  async post<T>(
    path: string,
    body: Record<string, any>,
    options?: {
      query?: Record<string, any>;
      headers?: Record<string, string>;
      projectId?: string;
    }
  ): Promise<T> {
    return this.request<T>('POST', path, { body, ...options });
  }

  /**
   * PUT request
   */
  async put<T>(
    path: string,
    body?: Record<string, any>,
    options?: {
      query?: Record<string, any>;
      headers?: Record<string, string>;
      projectId?: string;
    }
  ): Promise<T> {
    return this.request<T>('PUT', path, { body, ...options });
  }

  /**
   * DELETE request
   */
  async delete<T>(
    path: string,
    options?: {
      query?: Record<string, any>;
      headers?: Record<string, string>;
      projectId?: string;
    }
  ): Promise<T> {
    return this.request<T>('DELETE', path, options);
  }

  /**
   * Build full URL with query parameters
   */
  private buildUrl(path: string, query?: Record<string, any>): string {
    const fullPath = this.baseUrl + path;
    if (!query || Object.keys(query).length === 0) {
      return fullPath;
    }

    const queryString = Object.entries(query)
      .filter(([, value]) => value !== undefined && value !== null && value !== '')
      .map(([key, value]) => {
        const encodedKey = encodeURIComponent(key);
        const encodedValue = encodeURIComponent(String(value));
        return `${encodedKey}=${encodedValue}`;
      })
      .join('&');

    return queryString ? `${fullPath}?${queryString}` : fullPath;
  }

  /**
   * Build request headers
   */
  private buildHeaders(
    customHeaders?: Record<string, string>,
    projectId?: string
  ): Record<string, string> {
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
      Authorization: this.getAuthHeader(),
      ...customHeaders,
    };

    if (projectId) {
      headers['X-Project-Id'] = projectId;
    }

    // For end-user endpoints, include X-Api-Key header
    if (this.endUserToken && !this.apiSecret) {
      headers['X-Api-Key'] = this.apiKey;
    }

    return headers;
  }

  /**
   * Fetch with timeout
   */
  private fetchWithTimeout(
    url: string,
    options: RequestInit
  ): Promise<Response> {
    return Promise.race([
      fetch(url, options),
      new Promise<Response>((_, reject) =>
        setTimeout(() => reject(new Error('Request timeout')), this.timeout)
      ),
    ]);
  }

  /**
   * Handle API response
   */
  private async handleResponse<T>(response: Response): Promise<T> {
    const contentType = response.headers.get('content-type');
    const isJson = contentType?.includes('application/json');

    if (!response.ok) {
      const errorData = isJson ? await response.json() : await response.text();
      throw new ApiError(
        response.status,
        this.extractErrorMessage(errorData),
        errorData
      );
    }

    // Handle 204 No Content
    if (response.status === 204) {
      return {} as T;
    }

    if (!isJson) {
      throw new Error(`Unexpected response type: ${contentType}`);
    }

    const data = await response.json();

    // Check if response follows our envelope format
    if (data.success === false) {
      throw new ApiError(response.status, data.error?.message || 'Unknown error', data.error);
    }

    return data.data ?? data;
  }

  /**
   * Extract error message from various error formats
   */
  private extractErrorMessage(error: any): string {
    if (typeof error === 'string') {
      return error;
    }
    if (error?.message) {
      return error.message;
    }
    if (error?.error) {
      return typeof error.error === 'string' ? error.error : JSON.stringify(error.error);
    }
    return 'Unknown error occurred';
  }

  /**
   * Handle errors
   */
  private handleError(error: any): never {
    if (error instanceof ApiError) {
      throw error;
    }
    if (error instanceof Error) {
      throw new ApiError(0, error.message);
    }
    throw new ApiError(0, 'Unknown error occurred');
  }
}

/**
 * Custom API error class
 */
export class ApiError extends Error {
  constructor(
    public status: number,
    message: string,
    public details?: any
  ) {
    super(message);
    this.name = 'ApiError';
  }
}
