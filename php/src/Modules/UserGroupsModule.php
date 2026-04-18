<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

use Sakha\CMS\Models\PaginatedResponse;

/**
 * User Groups module for managing hierarchical groups for end users
 * Base: /api/user-groups
 */
class UserGroupsModule extends BaseModule
{
    /**
     * List all user groups with pagination and filtering
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @param ?string $status Filter by status: active, inactive
     * @param ?string $parentId Filter by parent group ID
     * @param ?string $search Search by group name
     * @return PaginatedResponse
     */
    public function listGroups(
        int $page = 1,
        int $limit = 50,
        ?string $status = null,
        ?string $parentId = null,
        ?string $search = null,
    ): PaginatedResponse {
        $response = $this->httpClient->get('/api/user-groups', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
            'status' => $status,
            'parent_id' => $parentId,
            'search' => $search,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific user group
     *
     * @param string $groupId
     * @return array<string, mixed>
     */
    public function getGroup(string $groupId): array
    {
        return $this->httpClient->get("/api/user-groups/{$groupId}")['data'] ?? [];
    }

    /**
     * Create a new user group
     *
     * @param string $name Group name
     * @param ?string $description Group description
     * @param string $status Group status: active, inactive
     * @param ?string $parentId Parent group ID (for hierarchical structure)
     * @return array<string, mixed>
     */
    public function createGroup(
        string $name,
        ?string $description = null,
        string $status = 'active',
        ?string $parentId = null,
    ): array {
        $response = $this->httpClient->post('/api/user-groups', $this->buildQuery([
            'name' => $name,
            'description' => $description,
            'status' => $status,
            'parent_id' => $parentId,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update a user group
     *
     * @param string $groupId
     * @param ?string $name
     * @param ?string $description
     * @param ?string $status
     * @param ?string $parentId
     * @return array<string, mixed>
     */
    public function updateGroup(
        string $groupId,
        ?string $name = null,
        ?string $description = null,
        ?string $status = null,
        ?string $parentId = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/user-groups/{$groupId}",
            $this->buildQuery([
                'name' => $name,
                'description' => $description,
                'status' => $status,
                'parent_id' => $parentId,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete a user group
     *
     * @param string $groupId
     * @return void
     */
    public function deleteGroup(string $groupId): void
    {
        $this->httpClient->delete("/api/user-groups/{$groupId}");
    }

    // SUBGROUPS

    /**
     * List all subgroups for a group
     *
     * @param string $groupId
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @return PaginatedResponse
     */
    public function listSubgroups(string $groupId, int $page = 1, int $limit = 50): PaginatedResponse
    {
        $response = $this->httpClient->get(
            "/api/user-groups/{$groupId}/subgroups",
            $this->buildQuery([
                'page' => $page,
                'limit' => $limit,
            ]),
        );

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Add a subgroup to a group
     *
     * @param string $groupId Parent group ID
     * @param string $subgroupId Subgroup ID
     * @return array<string, mixed>
     */
    public function addSubgroup(string $groupId, string $subgroupId): array
    {
        $response = $this->httpClient->post(
            "/api/user-groups/{$groupId}/subgroups",
            ['subgroup_id' => $subgroupId],
        );

        return $response['data'] ?? [];
    }

    /**
     * Remove a subgroup from a group
     *
     * @param string $groupId
     * @param string $subgroupId
     * @return void
     */
    public function removeSubgroup(string $groupId, string $subgroupId): void
    {
        $this->httpClient->delete("/api/user-groups/{$groupId}/subgroups/{$subgroupId}");
    }

    // MEMBERS

    /**
     * List all members in a group
     *
     * @param string $groupId
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @return PaginatedResponse
     */
    public function listMembers(string $groupId, int $page = 1, int $limit = 50): PaginatedResponse
    {
        $response = $this->httpClient->get(
            "/api/user-groups/{$groupId}/members",
            $this->buildQuery([
                'page' => $page,
                'limit' => $limit,
            ]),
        );

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Add a member to a group
     *
     * @param string $groupId
     * @param string $endUserId End user ID
     * @return array<string, mixed>
     */
    public function addMember(string $groupId, string $endUserId): array
    {
        $response = $this->httpClient->post(
            "/api/user-groups/{$groupId}/members",
            ['end_user_id' => $endUserId],
        );

        return $response['data'] ?? [];
    }

    /**
     * Remove a member from a group
     *
     * @param string $groupId
     * @param string $endUserId
     * @return void
     */
    public function removeMember(string $groupId, string $endUserId): void
    {
        $this->httpClient->delete("/api/user-groups/{$groupId}/members/{$endUserId}");
    }
}
