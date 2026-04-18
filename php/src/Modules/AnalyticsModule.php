<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

/**
 * Analytics module for retrieving project analytics data
 * Base: /api/analytics
 */
class AnalyticsModule extends BaseModule
{
    /**
     * Get all analytics data in one call
     *
     * @param string $timeRange Time range: 7d, 30d, 90d, 1y
     * @return array<string, mixed>
     */
    public function getAll(string $timeRange = '30d'): array
    {
        return $this->httpClient->get('/api/analytics/all', $this->buildQuery([
            'timeRange' => $timeRange,
        ]))['data'] ?? [];
    }

    /**
     * Get overview analytics (visitors, page views, bounce rate, session duration)
     *
     * @param string $timeRange Time range: 7d, 30d, 90d, 1y
     * @return array<string, mixed>
     */
    public function getOverview(string $timeRange = '30d'): array
    {
        return $this->httpClient->get('/api/analytics/overview', $this->buildQuery([
            'timeRange' => $timeRange,
        ]))['data'] ?? [];
    }

    /**
     * Get traffic analytics (sources, devices, top pages)
     *
     * @param string $timeRange Time range: 7d, 30d, 90d, 1y
     * @return array<string, mixed>
     */
    public function getTraffic(string $timeRange = '30d'): array
    {
        return $this->httpClient->get('/api/analytics/traffic', $this->buildQuery([
            'timeRange' => $timeRange,
        ]))['data'] ?? [];
    }

    /**
     * Get donations analytics (total amount, total donations, average donation, top campaigns)
     *
     * @param string $timeRange Time range: 7d, 30d, 90d, 1y
     * @return array<string, mixed>
     */
    public function getDonations(string $timeRange = '30d'): array
    {
        return $this->httpClient->get('/api/analytics/donations', $this->buildQuery([
            'timeRange' => $timeRange,
        ]))['data'] ?? [];
    }

    /**
     * Get content analytics (total posts, total views, average views per post, top posts)
     *
     * @param string $timeRange Time range: 7d, 30d, 90d, 1y
     * @return array<string, mixed>
     */
    public function getContent(string $timeRange = '30d'): array
    {
        return $this->httpClient->get('/api/analytics/content', $this->buildQuery([
            'timeRange' => $timeRange,
        ]))['data'] ?? [];
    }

    /**
     * Get events analytics (total events, total attendees, average attendees, upcoming events, top events)
     *
     * @return array<string, mixed>
     */
    public function getEvents(): array
    {
        return $this->httpClient->get('/api/analytics/events')['data'] ?? [];
    }
}
