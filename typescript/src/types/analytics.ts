import { DateTime } from './common';

/**
 * Page view analytics response
 */
export interface PageViewStats {
  path: string;
  visitors: number;
  pageViews: number;
  avgDuration: string;
  bounceRate: number;
}

/**
 * Traffic source analytics response
 */
export interface TrafficSource {
  name: string;
  visitors: number;
  percentage: number;
}

/**
 * Device analytics response
 */
export interface DeviceStats {
  name: 'Desktop' | 'Mobile' | 'Tablet';
  visitors: number;
  percentage: number;
}

/**
 * Analytics overview response
 */
export interface AnalyticsOverview {
  totalVisitors: number;
  visitorsChange: number;
  pageViews: number;
  pageViewsChange: number;
  bounceRate: number;
  bounceRateChange: number;
  avgSessionDuration: string;
  sessionDurationChange: number;
}

/**
 * Analytics traffic response
 */
export interface AnalyticsTraffic {
  sources: TrafficSource[];
  devices: DeviceStats[];
  pages: PageViewStats[];
  referrers: Array<{
    referrer: string;
    visitors: number;
  }>;
}

/**
 * Analytics events response (conversions)
 */
export interface AnalyticsEvents {
  total: number;
  byType: Array<{
    type: string;
    count: number;
  }>;
  byPage: Array<{
    page: string;
    count: number;
  }>;
}

/**
 * Analytics dashboard response (aggregated)
 */
export interface AnalyticsDashboard {
  overview: AnalyticsOverview;
  traffic: AnalyticsTraffic;
  events: AnalyticsEvents;
  range: {
    start: DateTime;
    end: DateTime;
  };
}

/**
 * Analytics query parameters
 */
export interface AnalyticsQueryParams {
  timeRange?: '7d' | '30d' | '90d' | '1y';
  startDate?: DateTime;
  endDate?: DateTime;
}
