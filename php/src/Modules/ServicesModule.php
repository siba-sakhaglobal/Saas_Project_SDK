<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

use Sakha\CMS\Models\PaginatedResponse;

/**
 * Services module for managing project services
 * Base: /api/project-services
 */
class ServicesModule extends BaseModule
{
    /**
     * List all services with pagination and filtering
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @param ?string $status Filter by status: active, inactive
     * @param ?string $search Search by name
     * @return PaginatedResponse
     */
    public function listServices(
        int $page = 1,
        int $limit = 50,
        ?string $status = null,
        ?string $search = null,
    ): PaginatedResponse {
        $response = $this->httpClient->get('/api/project-services', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
            'status' => $status,
            'search' => $search,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific service by ID
     *
     * @param string $serviceId
     * @return array<string, mixed>
     */
    public function getService(string $serviceId): array
    {
        return $this->httpClient->get("/api/project-services/{$serviceId}")['data'] ?? [];
    }

    /**
     * Create a new service
     *
     * @param string $name Service name
     * @param string $description Service description
     * @param int $priceCents Service price in cents
     * @param string $status Service status
     * @param ?string $slug Service slug (auto-generated if not provided)
     * @param ?string $imageUrl Service image URL
     * @return array<string, mixed>
     */
    public function createService(
        string $name,
        string $description,
        int $priceCents,
        string $status = 'active',
        ?string $slug = null,
        ?string $imageUrl = null,
    ): array {
        $response = $this->httpClient->post('/api/project-services', $this->buildQuery([
            'name' => $name,
            'description' => $description,
            'price_cents' => $priceCents,
            'status' => $status,
            'slug' => $slug,
            'image_url' => $imageUrl,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update a service
     *
     * @param string $serviceId
     * @param ?string $name
     * @param ?string $description
     * @param ?int $priceCents
     * @param ?string $status
     * @param ?string $slug
     * @param ?string $imageUrl
     * @return array<string, mixed>
     */
    public function updateService(
        string $serviceId,
        ?string $name = null,
        ?string $description = null,
        ?int $priceCents = null,
        ?string $status = null,
        ?string $slug = null,
        ?string $imageUrl = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/project-services/{$serviceId}",
            $this->buildQuery([
                'name' => $name,
                'description' => $description,
                'price_cents' => $priceCents,
                'status' => $status,
                'slug' => $slug,
                'image_url' => $imageUrl,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete a service
     *
     * @param string $serviceId
     * @return void
     */
    public function deleteService(string $serviceId): void
    {
        $this->httpClient->delete("/api/project-services/{$serviceId}");
    }
}
