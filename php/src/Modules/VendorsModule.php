<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

use Sakha\CMS\Models\PaginatedResponse;

/**
 * Vendors module for managing project vendors
 * Base: /api/project-vendors
 */
class VendorsModule extends BaseModule
{
    /**
     * List all vendors with pagination and filtering
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @param ?string $status Filter by status: active, inactive
     * @param ?string $search Search by vendor name
     * @return PaginatedResponse
     */
    public function listVendors(
        int $page = 1,
        int $limit = 50,
        ?string $status = null,
        ?string $search = null,
    ): PaginatedResponse {
        $response = $this->httpClient->get('/api/project-vendors', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
            'status' => $status,
            'search' => $search,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific vendor by ID
     *
     * @param string $vendorId
     * @return array<string, mixed>
     */
    public function getVendor(string $vendorId): array
    {
        return $this->httpClient->get("/api/project-vendors/{$vendorId}")['data'] ?? [];
    }

    /**
     * Create a new vendor
     *
     * @param string $name Vendor name
     * @param string $email Vendor email
     * @param ?string $phone Vendor phone
     * @param ?string $address Vendor address
     * @param ?float $commissionPercentage Commission percentage (0-100)
     * @param string $status Vendor status
     * @return array<string, mixed>
     */
    public function createVendor(
        string $name,
        string $email,
        ?string $phone = null,
        ?string $address = null,
        ?float $commissionPercentage = null,
        string $status = 'active',
    ): array {
        $response = $this->httpClient->post('/api/project-vendors', $this->buildQuery([
            'name' => $name,
            'email' => $email,
            'phone' => $phone,
            'address' => $address,
            'commission_percentage' => $commissionPercentage,
            'status' => $status,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update a vendor
     *
     * @param string $vendorId
     * @param ?string $name
     * @param ?string $email
     * @param ?string $phone
     * @param ?string $address
     * @param ?float $commissionPercentage
     * @param ?string $status
     * @return array<string, mixed>
     */
    public function updateVendor(
        string $vendorId,
        ?string $name = null,
        ?string $email = null,
        ?string $phone = null,
        ?string $address = null,
        ?float $commissionPercentage = null,
        ?string $status = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/project-vendors/{$vendorId}",
            $this->buildQuery([
                'name' => $name,
                'email' => $email,
                'phone' => $phone,
                'address' => $address,
                'commission_percentage' => $commissionPercentage,
                'status' => $status,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete a vendor
     *
     * @param string $vendorId
     * @return void
     */
    public function deleteVendor(string $vendorId): void
    {
        $this->httpClient->delete("/api/project-vendors/{$vendorId}");
    }
}
