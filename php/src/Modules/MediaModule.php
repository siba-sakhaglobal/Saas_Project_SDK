<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

use Sakha\CMS\Models\PaginatedResponse;

/**
 * Media module for managing file uploads and S3 integration
 * Base: /api/media
 */
class MediaModule extends BaseModule
{
    /**
     * List all media files with pagination and filtering
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @param ?string $category Filter by category (images, documents, videos)
     * @param ?string $search Search by filename
     * @return PaginatedResponse
     */
    public function listMedia(
        int $page = 1,
        int $limit = 50,
        ?string $category = null,
        ?string $search = null,
    ): PaginatedResponse {
        $response = $this->httpClient->get('/api/media', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
            'category' => $category,
            'search' => $search,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific media file
     *
     * @param string $mediaId
     * @return array<string, mixed>
     */
    public function getMedia(string $mediaId): array
    {
        return $this->httpClient->get("/api/media/{$mediaId}")['data'] ?? [];
    }

    /**
     * Get presigned upload URL for S3
     *
     * @param string $filename Filename to upload
     * @param string $contentType MIME type (e.g., image/png, application/pdf)
     * @param ?string $category File category (images, documents, videos)
     * @return array<string, mixed> Contains presigned_url and fields for upload
     */
    public function getPresignedUploadUrl(
        string $filename,
        string $contentType,
        ?string $category = null,
    ): array {
        $response = $this->httpClient->post('/api/media/presigned-upload', $this->buildQuery([
            'filename' => $filename,
            'content_type' => $contentType,
            'category' => $category,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Create a media file record after uploading to S3
     *
     * @param string $filename Filename
     * @param string $s3Url S3 URL after upload
     * @param string $contentType MIME type
     * @param int $fileSizeBytes File size in bytes
     * @param ?string $category File category
     * @return array<string, mixed>
     */
    public function createMedia(
        string $filename,
        string $s3Url,
        string $contentType,
        int $fileSizeBytes,
        ?string $category = null,
    ): array {
        $response = $this->httpClient->post('/api/media', $this->buildQuery([
            'filename' => $filename,
            's3_url' => $s3Url,
            'content_type' => $contentType,
            'file_size_bytes' => $fileSizeBytes,
            'category' => $category,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update a media file record
     *
     * @param string $mediaId
     * @param ?string $filename
     * @param ?string $category
     * @return array<string, mixed>
     */
    public function updateMedia(
        string $mediaId,
        ?string $filename = null,
        ?string $category = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/media/{$mediaId}",
            $this->buildQuery([
                'filename' => $filename,
                'category' => $category,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete a media file
     *
     * @param string $mediaId
     * @return void
     */
    public function deleteMedia(string $mediaId): void
    {
        $this->httpClient->delete("/api/media/{$mediaId}");
    }

    /**
     * Get presigned download URL for a file
     *
     * @param string $mediaId
     * @param ?int $expirationSeconds URL expiration in seconds (default: 3600)
     * @return array<string, mixed> Contains download_url
     */
    public function getPresignedDownloadUrl(string $mediaId, ?int $expirationSeconds = null): array
    {
        $response = $this->httpClient->get(
            "/api/media/{$mediaId}/download-url",
            $this->buildQuery([
                'expiration_seconds' => $expirationSeconds,
            ]),
        );

        return $response['data'] ?? [];
    }
}
