<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

use Sakha\CMS\Models\PaginatedResponse;

/**
 * Donations module for managing donation campaigns and donations
 * Base: /api/donations
 */
class DonationsModule extends BaseModule
{
    /**
     * List all donation campaigns with pagination and filtering
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @param ?string $status Filter by status: active, inactive, closed
     * @param ?string $search Search by campaign name
     * @return PaginatedResponse
     */
    public function listCampaigns(
        int $page = 1,
        int $limit = 50,
        ?string $status = null,
        ?string $search = null,
    ): PaginatedResponse {
        $response = $this->httpClient->get('/api/donations/campaigns', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
            'status' => $status,
            'search' => $search,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific donation campaign by ID
     *
     * @param string $campaignId
     * @return array<string, mixed>
     */
    public function getCampaign(string $campaignId): array
    {
        return $this->httpClient->get("/api/donations/campaigns/{$campaignId}")['data'] ?? [];
    }

    /**
     * Create a new donation campaign
     *
     * @param string $name Campaign name
     * @param string $description Campaign description
     * @param int $goalAmountCents Goal amount in cents
     * @param ?string $featuredImageUrl Featured image URL
     * @param string $status Status: active, inactive, closed
     * @return array<string, mixed>
     */
    public function createCampaign(
        string $name,
        string $description,
        int $goalAmountCents,
        ?string $featuredImageUrl = null,
        string $status = 'active',
    ): array {
        $response = $this->httpClient->post('/api/donations/campaigns', $this->buildQuery([
            'name' => $name,
            'description' => $description,
            'goal_amount_cents' => $goalAmountCents,
            'featured_image_url' => $featuredImageUrl,
            'status' => $status,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update a donation campaign
     *
     * @param string $campaignId
     * @param ?string $name
     * @param ?string $description
     * @param ?int $goalAmountCents
     * @param ?string $featuredImageUrl
     * @param ?string $status
     * @return array<string, mixed>
     */
    public function updateCampaign(
        string $campaignId,
        ?string $name = null,
        ?string $description = null,
        ?int $goalAmountCents = null,
        ?string $featuredImageUrl = null,
        ?string $status = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/donations/campaigns/{$campaignId}",
            $this->buildQuery([
                'name' => $name,
                'description' => $description,
                'goal_amount_cents' => $goalAmountCents,
                'featured_image_url' => $featuredImageUrl,
                'status' => $status,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete a donation campaign
     *
     * @param string $campaignId
     * @return void
     */
    public function deleteCampaign(string $campaignId): void
    {
        $this->httpClient->delete("/api/donations/campaigns/{$campaignId}");
    }

    /**
     * List all donations for a campaign
     *
     * @param string $campaignId
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @return PaginatedResponse
     */
    public function listDonations(
        string $campaignId,
        int $page = 1,
        int $limit = 50,
    ): PaginatedResponse {
        $response = $this->httpClient->get(
            "/api/donations/campaigns/{$campaignId}/donations",
            $this->buildQuery([
                'page' => $page,
                'limit' => $limit,
            ]),
        );

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific donation by ID
     *
     * @param string $campaignId
     * @param string $donationId
     * @return array<string, mixed>
     */
    public function getDonation(string $campaignId, string $donationId): array
    {
        return $this->httpClient->get(
            "/api/donations/campaigns/{$campaignId}/donations/{$donationId}",
        )['data'] ?? [];
    }

    /**
     * Create a new donation
     *
     * @param string $campaignId
     * @param int $amountCents Donation amount in cents
     * @param ?string $donorName Donor name
     * @param ?string $donorEmail Donor email
     * @param ?string $donorPhone Donor phone
     * @param ?string $message Donation message
     * @return array<string, mixed>
     */
    public function createDonation(
        string $campaignId,
        int $amountCents,
        ?string $donorName = null,
        ?string $donorEmail = null,
        ?string $donorPhone = null,
        ?string $message = null,
    ): array {
        $response = $this->httpClient->post(
            "/api/donations/campaigns/{$campaignId}/donations",
            $this->buildQuery([
                'amount_cents' => $amountCents,
                'donor_name' => $donorName,
                'donor_email' => $donorEmail,
                'donor_phone' => $donorPhone,
                'message' => $message,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Update a donation
     *
     * @param string $campaignId
     * @param string $donationId
     * @param ?int $amountCents
     * @param ?string $donorName
     * @param ?string $donorEmail
     * @param ?string $donorPhone
     * @param ?string $message
     * @return array<string, mixed>
     */
    public function updateDonation(
        string $campaignId,
        string $donationId,
        ?int $amountCents = null,
        ?string $donorName = null,
        ?string $donorEmail = null,
        ?string $donorPhone = null,
        ?string $message = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/donations/campaigns/{$campaignId}/donations/{$donationId}",
            $this->buildQuery([
                'amount_cents' => $amountCents,
                'donor_name' => $donorName,
                'donor_email' => $donorEmail,
                'donor_phone' => $donorPhone,
                'message' => $message,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete a donation
     *
     * @param string $campaignId
     * @param string $donationId
     * @return void
     */
    public function deleteDonation(string $campaignId, string $donationId): void
    {
        $this->httpClient->delete(
            "/api/donations/campaigns/{$campaignId}/donations/{$donationId}",
        );
    }
}
