import { HttpClient } from '../client';
import type {
  AnalyticsOverview,
  AnalyticsTraffic,
  AnalyticsEvents,
  AnalyticsDashboard,
  AnalyticsQueryParams,
} from '../types/analytics';

export class AnalyticsModule {
  constructor(private client: HttpClient) {}

  /**
   * Get analytics overview (overview section of dashboard)
   */
  async getOverview(params?: AnalyticsQueryParams): Promise<AnalyticsOverview> {
    return this.client.get<AnalyticsOverview>('/api/analytics/overview', { params });
  }

  /**
   * Get analytics traffic data (sources, devices, pages)
   */
  async getTraffic(params?: AnalyticsQueryParams): Promise<AnalyticsTraffic> {
    return this.client.get<AnalyticsTraffic>('/api/analytics/traffic', { params });
  }

  /**
   * Get analytics events data (conversions/goal tracking)
   */
  async getEvents(params?: AnalyticsQueryParams): Promise<AnalyticsEvents> {
    return this.client.get<AnalyticsEvents>('/api/analytics/all', { params });
  }

  /**
   * Get full analytics dashboard (all sections combined)
   */
  async getDashboard(params?: AnalyticsQueryParams): Promise<AnalyticsDashboard> {
    return this.client.get<AnalyticsDashboard>('/api/analytics/all', { params });
  }
}
