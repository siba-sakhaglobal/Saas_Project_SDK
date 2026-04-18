<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

use Sakha\CMS\Models\PaginatedResponse;

/**
 * Banners module for managing project banners
 * Base: /api/project-banners
 */
class BannersModule extends BaseModule
{
    /**
     * List all banners with pagination and filtering
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @param ?string $placement Filter by placement: hero, sidebar, footer, popup
     * @param ?string $status Filter by status: active, inactive
     * @return PaginatedResponse
     */
    public function listBanners(
        int $page = 1,
        int $limit = 50,
        ?string $placement = null,
        ?string $status = null,
    ): PaginatedResponse {
        $response = $this->httpClient->get('/api/project-banners', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
            'placement' => $placement,
            'status' => $status,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific banner by ID
     *
     * @param string $bannerId
     * @return array<string, mixed>
     */
    public function getBanner(string $bannerId): array
    {
        return $this->httpClient->get("/api/project-banners/{$bannerId}")['data'] ?? [];
    }

    /**
     * Create a new banner
     *
     * @param string $title Banner title
     * @param string $content Banner content
     * @param string $placement Banner placement: hero, sidebar, footer, popup
     * @param string $status Banner status
     * @param ?string $imageUrl Banner image URL
     * @param ?string $ctaUrl Call-to-action URL
     * @param ?string $ctaText Call-to-action text
     * @return array<string, mixed>
     */
    public function createBanner(
        string $title,
        string $content,
        string $placement,
        string $status = 'active',
        ?string $imageUrl = null,
        ?string $ctaUrl = null,
        ?string $ctaText = null,
    ): array {
        $response = $this->httpClient->post('/api/project-banners', $this->buildQuery([
            'title' => $title,
            'content' => $content,
            'placement' => $placement,
            'status' => $status,
            'image_url' => $imageUrl,
            'cta_url' => $ctaUrl,
            'cta_text' => $ctaText,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update a banner
     *
     * @param string $bannerId
     * @param ?string $title
     * @param ?string $content
     * @param ?string $placement
     * @param ?string $status
     * @param ?string $imageUrl
     * @param ?string $ctaUrl
     * @param ?string $ctaText
     * @return array<string, mixed>
     */
    public function updateBanner(
        string $bannerId,
        ?string $title = null,
        ?string $content = null,
        ?string $placement = null,
        ?string $status = null,
        ?string $imageUrl = null,
        ?string $ctaUrl = null,
        ?string $ctaText = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/project-banners/{$bannerId}",
            $this->buildQuery([
                'title' => $title,
                'content' => $content,
                'placement' => $placement,
                'status' => $status,
                'image_url' => $imageUrl,
                'cta_url' => $ctaUrl,
                'cta_text' => $ctaText,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete a banner
     *
     * @param string $bannerId
     * @return void
     */
    public function deleteBanner(string $bannerId): void
    {
        $this->httpClient->delete("/api/project-banners/{$bannerId}");
    }
}
