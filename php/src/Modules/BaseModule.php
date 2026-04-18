<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

use Sakha\CMS\HttpClient;
use Sakha\CMS\Models\ApiResponse;
use Sakha\CMS\Models\PaginatedResponse;

/**
 * Base module class for all API modules
 */
abstract class BaseModule
{
    protected HttpClient $httpClient;

    public function __construct(HttpClient $httpClient)
    {
        $this->httpClient = $httpClient;
    }

    /**
     * Parse API response into ApiResponse object
     *
     * @param array<string, mixed> $response
     * @return ApiResponse
     */
    protected function parseResponse(array $response): ApiResponse
    {
        return ApiResponse::fromArray($response);
    }

    /**
     * Parse paginated API response
     *
     * @param array<string, mixed> $response
     * @return PaginatedResponse
     */
    protected function parsePaginatedResponse(array $response): PaginatedResponse
    {
        return PaginatedResponse::fromArray($response);
    }

    /**
     * Build query parameters, filtering out null values
     *
     * @param array<string, mixed> $params
     * @return array<string, mixed>
     */
    protected function buildQuery(array $params): array
    {
        return array_filter($params, static fn($value) => $value !== null);
    }
}
