<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

use Sakha\CMS\Models\PaginatedResponse;

/**
 * Team module for managing team members with different roles
 * Base: /api/team
 */
class TeamModule extends BaseModule
{
    /**
     * List all team members with pagination and filtering
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @param ?string $role Filter by role: board, staff, volunteer, advisor
     * @param ?string $status Filter by status: active, inactive
     * @param ?string $search Search by name or email
     * @return PaginatedResponse
     */
    public function listMembers(
        int $page = 1,
        int $limit = 50,
        ?string $role = null,
        ?string $status = null,
        ?string $search = null,
    ): PaginatedResponse {
        $response = $this->httpClient->get('/api/team', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
            'role' => $role,
            'status' => $status,
            'search' => $search,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific team member
     *
     * @param string $memberId
     * @return array<string, mixed>
     */
    public function getMember(string $memberId): array
    {
        return $this->httpClient->get("/api/team/{$memberId}")['data'] ?? [];
    }

    /**
     * Create a new team member
     *
     * @param string $email Member email
     * @param string $name Member full name
     * @param string $role Member role: board, staff, volunteer, advisor
     * @param string $status Member status: active, inactive
     * @param ?string $phone Member phone
     * @param ?string $position Member position/title
     * @return array<string, mixed>
     */
    public function createMember(
        string $email,
        string $name,
        string $role,
        string $status = 'active',
        ?string $phone = null,
        ?string $position = null,
    ): array {
        $response = $this->httpClient->post('/api/team', $this->buildQuery([
            'email' => $email,
            'name' => $name,
            'role' => $role,
            'status' => $status,
            'phone' => $phone,
            'position' => $position,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update a team member
     *
     * @param string $memberId
     * @param ?string $email
     * @param ?string $name
     * @param ?string $role
     * @param ?string $status
     * @param ?string $phone
     * @param ?string $position
     * @return array<string, mixed>
     */
    public function updateMember(
        string $memberId,
        ?string $email = null,
        ?string $name = null,
        ?string $role = null,
        ?string $status = null,
        ?string $phone = null,
        ?string $position = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/team/{$memberId}",
            $this->buildQuery([
                'email' => $email,
                'name' => $name,
                'role' => $role,
                'status' => $status,
                'phone' => $phone,
                'position' => $position,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete a team member
     *
     * @param string $memberId
     * @return void
     */
    public function deleteMember(string $memberId): void
    {
        $this->httpClient->delete("/api/team/{$memberId}");
    }
}
