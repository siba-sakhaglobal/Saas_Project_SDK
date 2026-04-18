<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

use Sakha\CMS\Models\PaginatedResponse;

/**
 * Blog module for managing blog posts and categories
 * Base: /api/blog
 */
class BlogModule extends BaseModule
{
    /**
     * List all blog posts with pagination and filtering
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50, max: 100)
     * @param ?string $status Filter by status: draft, published, archived
     * @param ?string $categoryId Filter by category ID
     * @param ?string $search Search by title or content
     * @return PaginatedResponse
     */
    public function listPosts(
        int $page = 1,
        int $limit = 50,
        ?string $status = null,
        ?string $categoryId = null,
        ?string $search = null,
    ): PaginatedResponse {
        $response = $this->httpClient->get('/api/blog/posts', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
            'status' => $status,
            'category_id' => $categoryId,
            'search' => $search,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific blog post by ID
     *
     * @param string $postId
     * @return array<string, mixed>
     */
    public function getPost(string $postId): array
    {
        return $this->httpClient->get("/api/blog/posts/{$postId}")['data'] ?? [];
    }

    /**
     * Create a new blog post
     *
     * @param string $title Post title
     * @param string $content Post content (HTML)
     * @param string $status Status: draft, published, archived
     * @param ?string $excerpt Short excerpt
     * @param ?string $featuredImageUrl Featured image URL
     * @param ?string $categoryId Category ID
     * @param array<string> $tags Tag names
     * @return array<string, mixed>
     */
    public function createPost(
        string $title,
        string $content,
        string $status = 'draft',
        ?string $excerpt = null,
        ?string $featuredImageUrl = null,
        ?string $categoryId = null,
        array $tags = [],
    ): array {
        $response = $this->httpClient->post('/api/blog/posts', $this->buildQuery([
            'title' => $title,
            'content' => $content,
            'status' => $status,
            'excerpt' => $excerpt,
            'featured_image_url' => $featuredImageUrl,
            'category_id' => $categoryId,
            'tags' => $tags ?: null,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update a blog post
     *
     * @param string $postId
     * @param ?string $title
     * @param ?string $content
     * @param ?string $status
     * @param ?string $excerpt
     * @param ?string $featuredImageUrl
     * @param ?string $categoryId
     * @param ?array<string> $tags
     * @return array<string, mixed>
     */
    public function updatePost(
        string $postId,
        ?string $title = null,
        ?string $content = null,
        ?string $status = null,
        ?string $excerpt = null,
        ?string $featuredImageUrl = null,
        ?string $categoryId = null,
        ?array $tags = null,
    ): array {
        $response = $this->httpClient->put("/api/blog/posts/{$postId}", $this->buildQuery([
            'title' => $title,
            'content' => $content,
            'status' => $status,
            'excerpt' => $excerpt,
            'featured_image_url' => $featuredImageUrl,
            'category_id' => $categoryId,
            'tags' => $tags,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Delete a blog post
     *
     * @param string $postId
     * @return void
     */
    public function deletePost(string $postId): void
    {
        $this->httpClient->delete("/api/blog/posts/{$postId}");
    }

    /**
     * List all blog categories
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @return PaginatedResponse
     */
    public function listCategories(int $page = 1, int $limit = 50): PaginatedResponse
    {
        $response = $this->httpClient->get('/api/blog/categories', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific blog category
     *
     * @param string $categoryId
     * @return array<string, mixed>
     */
    public function getCategory(string $categoryId): array
    {
        return $this->httpClient->get("/api/blog/categories/{$categoryId}")['data'] ?? [];
    }

    /**
     * Create a new blog category
     *
     * @param string $name Category name
     * @param ?string $description Category description
     * @return array<string, mixed>
     */
    public function createCategory(string $name, ?string $description = null): array
    {
        $response = $this->httpClient->post('/api/blog/categories', $this->buildQuery([
            'name' => $name,
            'description' => $description,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update a blog category
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
            "/api/blog/categories/{$categoryId}",
            $this->buildQuery([
                'name' => $name,
                'description' => $description,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete a blog category
     *
     * @param string $categoryId
     * @return void
     */
    public function deleteCategory(string $categoryId): void
    {
        $this->httpClient->delete("/api/blog/categories/{$categoryId}");
    }
}
