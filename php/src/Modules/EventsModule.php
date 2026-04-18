<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

use Sakha\CMS\Models\PaginatedResponse;

/**
 * Events module for managing events and categories
 * Base: /api/events
 */
class EventsModule extends BaseModule
{
    /**
     * List all events with pagination and filtering
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @param ?string $status Filter by status: scheduled, ongoing, completed, cancelled
     * @param ?string $categoryId Filter by category ID
     * @param ?string $search Search by title or description
     * @return PaginatedResponse
     */
    public function listEvents(
        int $page = 1,
        int $limit = 50,
        ?string $status = null,
        ?string $categoryId = null,
        ?string $search = null,
    ): PaginatedResponse {
        $response = $this->httpClient->get('/api/events', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
            'status' => $status,
            'category_id' => $categoryId,
            'search' => $search,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific event by ID
     *
     * @param string $eventId
     * @return array<string, mixed>
     */
    public function getEvent(string $eventId): array
    {
        return $this->httpClient->get("/api/events/{$eventId}")['data'] ?? [];
    }

    /**
     * Create a new event
     *
     * @param string $title Event title
     * @param string $description Event description
     * @param string $startDate Start date (ISO 8601)
     * @param string $endDate End date (ISO 8601)
     * @param string $location Event location
     * @param int $capacity Total capacity
     * @param int $registrations Current registrations (default: 0)
     * @param ?string $featuredImageUrl Featured image URL
     * @param ?string $categoryId Category ID
     * @param string $status Status: scheduled, ongoing, completed, cancelled
     * @return array<string, mixed>
     */
    public function createEvent(
        string $title,
        string $description,
        string $startDate,
        string $endDate,
        string $location,
        int $capacity,
        ?string $featuredImageUrl = null,
        ?string $categoryId = null,
        string $status = 'scheduled',
        int $registrations = 0,
    ): array {
        $response = $this->httpClient->post('/api/events', $this->buildQuery([
            'title' => $title,
            'description' => $description,
            'start_date' => $startDate,
            'end_date' => $endDate,
            'location' => $location,
            'capacity' => $capacity,
            'registrations' => $registrations,
            'featured_image_url' => $featuredImageUrl,
            'category_id' => $categoryId,
            'status' => $status,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update an event
     *
     * @param string $eventId
     * @param ?string $title
     * @param ?string $description
     * @param ?string $startDate
     * @param ?string $endDate
     * @param ?string $location
     * @param ?int $capacity
     * @param ?int $registrations
     * @param ?string $featuredImageUrl
     * @param ?string $categoryId
     * @param ?string $status
     * @return array<string, mixed>
     */
    public function updateEvent(
        string $eventId,
        ?string $title = null,
        ?string $description = null,
        ?string $startDate = null,
        ?string $endDate = null,
        ?string $location = null,
        ?int $capacity = null,
        ?int $registrations = null,
        ?string $featuredImageUrl = null,
        ?string $categoryId = null,
        ?string $status = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/events/{$eventId}",
            $this->buildQuery([
                'title' => $title,
                'description' => $description,
                'start_date' => $startDate,
                'end_date' => $endDate,
                'location' => $location,
                'capacity' => $capacity,
                'registrations' => $registrations,
                'featured_image_url' => $featuredImageUrl,
                'category_id' => $categoryId,
                'status' => $status,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete an event
     *
     * @param string $eventId
     * @return void
     */
    public function deleteEvent(string $eventId): void
    {
        $this->httpClient->delete("/api/events/{$eventId}");
    }

    /**
     * List all event categories
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @return PaginatedResponse
     */
    public function listCategories(int $page = 1, int $limit = 50): PaginatedResponse
    {
        $response = $this->httpClient->get('/api/events/categories', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific event category
     *
     * @param string $categoryId
     * @return array<string, mixed>
     */
    public function getCategory(string $categoryId): array
    {
        return $this->httpClient->get("/api/events/categories/{$categoryId}")['data'] ?? [];
    }

    /**
     * Create a new event category
     *
     * @param string $name Category name
     * @param ?string $description Category description
     * @return array<string, mixed>
     */
    public function createCategory(string $name, ?string $description = null): array
    {
        $response = $this->httpClient->post('/api/events/categories', $this->buildQuery([
            'name' => $name,
            'description' => $description,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update an event category
     *
     * @param string $categoryId
     * @param ?string $name
     * @param ?string $description
     * @return array<string, mixed>
     */
    public function updateCategory(
        string $categoryId,
        ?string $name = null,
        ?string $description = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/events/categories/{$categoryId}",
            $this->buildQuery([
                'name' => $name,
                'description' => $description,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete an event category
     *
     * @param string $categoryId
     * @return void
     */
    public function deleteCategory(string $categoryId): void
    {
        $this->httpClient->delete("/api/events/categories/{$categoryId}");
    }
}
