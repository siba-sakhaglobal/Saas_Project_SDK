/**
 * Sakha MicroSite CMS - TypeScript SDK
 * Production-grade SDK for accessing Sakha MicroSite CMS API
 * Supports both ESM and CommonJS exports
 */

export { HttpClient, ApiError } from './client';

// Type exports
export * from './types/common';
export * from './types/blog';
export * from './types/events';
export * from './types/donations';
export * from './types/orders';
export * from './types/invoices';
export * from './types/transactions';
export * from './types/services';
export * from './types/appointments';
export * from './types/vendors';
export * from './types/shipments';
export * from './types/products';
export * from './types/banners';
export * from './types/team';
export * from './types/users';
export * from './types/media';
export * from './types/user-groups';
export * from './types/analytics';

// Module imports
import { HttpClient } from './client';
import { BlogModule } from './modules/blog';
import { EventsModule } from './modules/events';
import { DonationsModule } from './modules/donations';
import { OrdersModule } from './modules/orders';
import { InvoicesModule } from './modules/invoices';
import { TransactionsModule } from './modules/transactions';
import { ServicesModule } from './modules/services';
import { AppointmentsModule } from './modules/appointments';
import { VendorsModule } from './modules/vendors';
import { ShipmentsModule } from './modules/shipments';
import { ProductsModule } from './modules/products';
import { BannersModule } from './modules/banners';
import { TeamModule } from './modules/team';
import { UsersModule } from './modules/users';
import { MediaModule } from './modules/media';
import { UserGroupsModule } from './modules/user-groups';
import { AnalyticsModule } from './modules/analytics';

/**
 * Sakha CMS SDK
 *
 * Main SDK class that aggregates all API modules.
 * Initialize with your API configuration and use the module-specific properties.
 *
 * @example
 * ```typescript
 * // For admin/tenant operations with API key+secret
 * const cms = new SakhaCMS({
 *   baseUrl: 'https://api.sakha.example.com',
 *   apiKey: 'your-api-key',
 *   apiSecret: 'your-api-secret',
 * });
 *
 * // For end-user operations with JWT token
 * const cms = new SakhaCMS({
 *   baseUrl: 'https://api.sakha.example.com',
 *   token: 'jwt-token-from-login',
 * });
 *
 * // Use modules
 * const posts = await cms.blog.listPosts();
 * const events = await cms.events.listEvents();
 * ```
 */
export class SakhaCMS {
  private client: HttpClient;

  // Module instances
  readonly blog: BlogModule;
  readonly events: EventsModule;
  readonly donations: DonationsModule;
  readonly orders: OrdersModule;
  readonly invoices: InvoicesModule;
  readonly transactions: TransactionsModule;
  readonly services: ServicesModule;
  readonly appointments: AppointmentsModule;
  readonly vendors: VendorsModule;
  readonly shipments: ShipmentsModule;
  readonly products: ProductsModule;
  readonly banners: BannersModule;
  readonly team: TeamModule;
  readonly users: UsersModule;
  readonly media: MediaModule;
  readonly userGroups: UserGroupsModule;
  readonly analytics: AnalyticsModule;

  constructor(config: SakhaCMSConfig) {
    this.client = new HttpClient(config);

    // Initialize all modules with the HTTP client
    this.blog = new BlogModule(this.client);
    this.events = new EventsModule(this.client);
    this.donations = new DonationsModule(this.client);
    this.orders = new OrdersModule(this.client);
    this.invoices = new InvoicesModule(this.client);
    this.transactions = new TransactionsModule(this.client);
    this.services = new ServicesModule(this.client);
    this.appointments = new AppointmentsModule(this.client);
    this.vendors = new VendorsModule(this.client);
    this.shipments = new ShipmentsModule(this.client);
    this.products = new ProductsModule(this.client);
    this.banners = new BannersModule(this.client);
    this.team = new TeamModule(this.client);
    this.users = new UsersModule(this.client);
    this.media = new MediaModule(this.client);
    this.userGroups = new UserGroupsModule(this.client);
    this.analytics = new AnalyticsModule(this.client);
  }

  /**
   * Set the X-Project-Id header for project-scoped operations
   * Required for most API endpoints
   */
  setProjectId(projectId: string): void {
    this.client.setProjectId(projectId);
  }

  /**
   * Clear the X-Project-Id header
   */
  clearProjectId(): void {
    this.client.clearProjectId();
  }
}

/**
 * SDK Configuration
 */
export interface SakhaCMSConfig {
  /**
   * Base URL of the Sakha CMS API
   * @example 'https://api.sakha.example.com'
   */
  baseUrl: string;

  /**
   * API key for admin/tenant operations
   * Used with apiSecret for HMAC authentication
   * Mutually exclusive with token
   */
  apiKey?: string;

  /**
   * API secret for admin/tenant operations
   * Used with apiKey for HMAC authentication
   */
  apiSecret?: string;

  /**
   * JWT token for end-user operations
   * Obtained from login endpoint
   * Mutually exclusive with apiKey/apiSecret
   */
  token?: string;

  /**
   * Request timeout in milliseconds (default: 30000)
   */
  timeout?: number;

  /**
   * Custom headers to include in all requests
   */
  headers?: Record<string, string>;
}

export default SakhaCMS;
