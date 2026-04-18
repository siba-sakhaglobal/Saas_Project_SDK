<?php

declare(strict_types=1);

namespace Sakha\CMS\Models;

/**
 * Standard API response envelope
 *
 * @template T
 */
class ApiResponse
{
    /**
     * @param bool $success Whether the request was successful
     * @param mixed $data Response data payload
     * @param ?string $error Error message (if any)
     * @param array<string, mixed> $meta Additional metadata
     */
    public function __construct(
        public readonly bool $success,
        public readonly mixed $data,
        public readonly ?string $error = null,
        public readonly array $meta = [],
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
        return new self(
            success: $response['success'] ?? false,
            data: $response['data'] ?? null,
            error: $response['error'] ?? null,
            meta: $response['meta'] ?? [],
        );
    }

    /**
     * Check if response indicates success
     */
    public function isSuccess(): bool
    {
        return $this->success === true;
    }
}
