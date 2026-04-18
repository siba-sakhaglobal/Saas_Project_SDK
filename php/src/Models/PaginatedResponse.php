<?php

declare(strict_types=1);

namespace Sakha\CMS\Models;

/**
 * Paginated response envelope
 *
 * @template T
 */
class PaginatedResponse
{
    /**
     * @param bool $success Whether the request was successful
     * @param array<T> $data Array of items
     * @param int $total Total number of items
     * @param int $page Current page number
     * @param int $limit Items per page
     * @param ?string $error Error message (if any)
     */
    public function __construct(
        public readonly bool $success,
        public readonly array $data,
        public readonly int $total,
        public readonly int $page,
        public readonly int $limit,
        public readonly ?string $error = null,
    ) {
    }

    /**
     * Create from API response array
     *
     * @param array<string, mixed> $response
     * @return self
     */
    public static function fromArray(array $response): self
    {
        $meta = $response['meta'] ?? [];

        return new self(
            success: $response['success'] ?? false,
            data: $response['data'] ?? [],
            total: $meta['total'] ?? 0,
            page: $meta['page'] ?? 1,
            limit: $meta['limit'] ?? 50,
            error: $response['error'] ?? null,
        );
    }

    /**
     * Check if response indicates success
     */
    public function isSuccess(): bool
    {
        return $this->success === true;
    }

    /**
     * Calculate total pages
     */
    public function getTotalPages(): int
    {
        if ($this->limit === 0) {
            return 0;
        }
        return (int) ceil($this->total / $this->limit);
    }

    /**
     * Check if there are more pages
     */
    public function hasMorePages(): bool
    {
        return $this->page < $this->getTotalPages();
    }
}
