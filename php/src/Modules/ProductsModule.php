<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

use Sakha\CMS\Models\PaginatedResponse;

/**
 * Products module for managing project products with variants, attributes, categories, and inventory
 * Base: /api/products
 */
class ProductsModule extends BaseModule
{
    /**
     * List all products with pagination and filtering
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @param ?string $status Filter by status: active, inactive, discontinued
     * @param ?string $categoryId Filter by category ID
     * @param ?string $search Search by product name
     * @return PaginatedResponse
     */
    public function listProducts(
        int $page = 1,
        int $limit = 50,
        ?string $status = null,
        ?string $categoryId = null,
        ?string $search = null,
    ): PaginatedResponse {
        $response = $this->httpClient->get('/api/products', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
            'status' => $status,
            'category_id' => $categoryId,
            'search' => $search,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific product by ID
     *
     * @param string $productId
     * @return array<string, mixed>
     */
    public function getProduct(string $productId): array
    {
        return $this->httpClient->get("/api/products/{$productId}")['data'] ?? [];
    }

    /**
     * Create a new product
     *
     * @param string $name Product name
     * @param string $description Product description
     * @param int $priceCents Product price in cents
     * @param string $status Product status
     * @param ?string $sku Product SKU
     * @param ?string $slug Product slug (auto-generated if not provided)
     * @param ?string $categoryId Category ID
     * @param array<string> $tags Product tags
     * @param ?int $stock Stock quantity
     * @param ?array<string, mixed> $metadata Additional metadata
     * @return array<string, mixed>
     */
    public function createProduct(
        string $name,
        string $description,
        int $priceCents,
        string $status = 'active',
        ?string $sku = null,
        ?string $slug = null,
        ?string $categoryId = null,
        array $tags = [],
        ?int $stock = null,
        ?array $metadata = null,
    ): array {
        $response = $this->httpClient->post('/api/products', $this->buildQuery([
            'name' => $name,
            'description' => $description,
            'price_cents' => $priceCents,
            'status' => $status,
            'sku' => $sku,
            'slug' => $slug,
            'category_id' => $categoryId,
            'tags' => $tags ?: null,
            'stock' => $stock,
            'metadata' => $metadata,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update a product
     *
     * @param string $productId
     * @param ?string $name
     * @param ?string $description
     * @param ?int $priceCents
     * @param ?string $status
     * @param ?string $sku
     * @param ?string $slug
     * @param ?string $categoryId
     * @param ?array<string> $tags
     * @param ?int $stock
     * @param ?array<string, mixed> $metadata
     * @return array<string, mixed>
     */
    public function updateProduct(
        string $productId,
        ?string $name = null,
        ?string $description = null,
        ?int $priceCents = null,
        ?string $status = null,
        ?string $sku = null,
        ?string $slug = null,
        ?string $categoryId = null,
        ?array $tags = null,
        ?int $stock = null,
        ?array $metadata = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/products/{$productId}",
            $this->buildQuery([
                'name' => $name,
                'description' => $description,
                'price_cents' => $priceCents,
                'status' => $status,
                'sku' => $sku,
                'slug' => $slug,
                'category_id' => $categoryId,
                'tags' => $tags,
                'stock' => $stock,
                'metadata' => $metadata,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete a product
     *
     * @param string $productId
     * @return void
     */
    public function deleteProduct(string $productId): void
    {
        $this->httpClient->delete("/api/products/{$productId}");
    }

    // CATEGORIES

    /**
     * List all product categories
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @return PaginatedResponse
     */
    public function listCategories(int $page = 1, int $limit = 50): PaginatedResponse
    {
        $response = $this->httpClient->get('/api/products/categories', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific product category
     *
     * @param string $categoryId
     * @return array<string, mixed>
     */
    public function getCategory(string $categoryId): array
    {
        return $this->httpClient->get("/api/products/categories/{$categoryId}")['data'] ?? [];
    }

    /**
     * Create a new product category
     *
     * @param string $name Category name
     * @param ?string $description Category description
     * @param ?string $slug Category slug (auto-generated if not provided)
     * @return array<string, mixed>
     */
    public function createCategory(string $name, ?string $description = null, ?string $slug = null): array
    {
        $response = $this->httpClient->post('/api/products/categories', $this->buildQuery([
            'name' => $name,
            'description' => $description,
            'slug' => $slug,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update a product category
     *
     * @param string $categoryId
     * @param ?string $name
     * @param ?string $description
     * @param ?string $slug
     * @return array<string, mixed>
     */
    public function updateCategory(
        string $categoryId,
        ?string $name = null,
        ?string $description = null,
        ?string $slug = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/products/categories/{$categoryId}",
            $this->buildQuery([
                'name' => $name,
                'description' => $description,
                'slug' => $slug,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete a product category
     *
     * @param string $categoryId
     * @return void
     */
    public function deleteCategory(string $categoryId): void
    {
        $this->httpClient->delete("/api/products/categories/{$categoryId}");
    }

    // VARIANTS

    /**
     * List all variants for a product
     *
     * @param string $productId
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @return PaginatedResponse
     */
    public function listVariants(string $productId, int $page = 1, int $limit = 50): PaginatedResponse
    {
        $response = $this->httpClient->get(
            "/api/products/{$productId}/variants",
            $this->buildQuery([
                'page' => $page,
                'limit' => $limit,
            ]),
        );

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific product variant
     *
     * @param string $productId
     * @param string $variantId
     * @return array<string, mixed>
     */
    public function getVariant(string $productId, string $variantId): array
    {
        return $this->httpClient->get(
            "/api/products/{$productId}/variants/{$variantId}",
        )['data'] ?? [];
    }

    /**
     * Create a new product variant
     *
     * @param string $productId
     * @param string $name Variant name (e.g., "Red - Small")
     * @param ?int $priceCents Variant price in cents (null to use product price)
     * @param ?string $sku Variant SKU
     * @param ?int $stock Stock quantity
     * @param array<string, string> $attributes Variant attributes (e.g., {"color": "red", "size": "small"})
     * @return array<string, mixed>
     */
    public function createVariant(
        string $productId,
        string $name,
        ?int $priceCents = null,
        ?string $sku = null,
        ?int $stock = null,
        array $attributes = [],
    ): array {
        $response = $this->httpClient->post(
            "/api/products/{$productId}/variants",
            $this->buildQuery([
                'name' => $name,
                'price_cents' => $priceCents,
                'sku' => $sku,
                'stock' => $stock,
                'attributes' => $attributes ?: null,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Update a product variant
     *
     * @param string $productId
     * @param string $variantId
     * @param ?string $name
     * @param ?int $priceCents
     * @param ?string $sku
     * @param ?int $stock
     * @param ?array<string, string> $attributes
     * @return array<string, mixed>
     */
    public function updateVariant(
        string $productId,
        string $variantId,
        ?string $name = null,
        ?int $priceCents = null,
        ?string $sku = null,
        ?int $stock = null,
        ?array $attributes = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/products/{$productId}/variants/{$variantId}",
            $this->buildQuery([
                'name' => $name,
                'price_cents' => $priceCents,
                'sku' => $sku,
                'stock' => $stock,
                'attributes' => $attributes,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete a product variant
     *
     * @param string $productId
     * @param string $variantId
     * @return void
     */
    public function deleteVariant(string $productId, string $variantId): void
    {
        $this->httpClient->delete("/api/products/{$productId}/variants/{$variantId}");
    }

    // ATTRIBUTES

    /**
     * List all product attributes
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @return PaginatedResponse
     */
    public function listAttributes(int $page = 1, int $limit = 50): PaginatedResponse
    {
        $response = $this->httpClient->get('/api/products/attributes', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific product attribute
     *
     * @param string $attributeId
     * @return array<string, mixed>
     */
    public function getAttribute(string $attributeId): array
    {
        return $this->httpClient->get("/api/products/attributes/{$attributeId}")['data'] ?? [];
    }

    /**
     * Create a new product attribute
     *
     * @param string $name Attribute name (e.g., "Color")
     * @param array<string> $values Attribute values (e.g., ["Red", "Blue", "Green"])
     * @return array<string, mixed>
     */
    public function createAttribute(string $name, array $values = []): array
    {
        $response = $this->httpClient->post(
            '/api/products/attributes',
            $this->buildQuery([
                'name' => $name,
                'values' => $values ?: null,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Update a product attribute
     *
     * @param string $attributeId
     * @param ?string $name
     * @param ?array<string> $values
     * @return array<string, mixed>
     */
    public function updateAttribute(string $attributeId, ?string $name = null, ?array $values = null): array
    {
        $response = $this->httpClient->put(
            "/api/products/attributes/{$attributeId}",
            $this->buildQuery([
                'name' => $name,
                'values' => $values,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete a product attribute
     *
     * @param string $attributeId
     * @return void
     */
    public function deleteAttribute(string $attributeId): void
    {
        $this->httpClient->delete("/api/products/attributes/{$attributeId}");
    }

    // IMAGES

    /**
     * List all images for a product
     *
     * @param string $productId
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @return PaginatedResponse
     */
    public function listImages(string $productId, int $page = 1, int $limit = 50): PaginatedResponse
    {
        $response = $this->httpClient->get(
            "/api/products/{$productId}/images",
            $this->buildQuery([
                'page' => $page,
                'limit' => $limit,
            ]),
        );

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific product image
     *
     * @param string $productId
     * @param string $imageId
     * @return array<string, mixed>
     */
    public function getImage(string $productId, string $imageId): array
    {
        return $this->httpClient->get("/api/products/{$productId}/images/{$imageId}")['data'] ?? [];
    }

    /**
     * Add an image to a product
     *
     * @param string $productId
     * @param string $url Image URL
     * @param ?int $sortOrder Sort order (for display order)
     * @param ?bool $isFeatured Mark as featured/primary image
     * @return array<string, mixed>
     */
    public function createImage(
        string $productId,
        string $url,
        ?int $sortOrder = null,
        ?bool $isFeatured = null,
    ): array {
        $response = $this->httpClient->post(
            "/api/products/{$productId}/images",
            $this->buildQuery([
                'url' => $url,
                'sort_order' => $sortOrder,
                'is_featured' => $isFeatured,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Update a product image
     *
     * @param string $productId
     * @param string $imageId
     * @param ?string $url
     * @param ?int $sortOrder
     * @param ?bool $isFeatured
     * @return array<string, mixed>
     */
    public function updateImage(
        string $productId,
        string $imageId,
        ?string $url = null,
        ?int $sortOrder = null,
        ?bool $isFeatured = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/products/{$productId}/images/{$imageId}",
            $this->buildQuery([
                'url' => $url,
                'sort_order' => $sortOrder,
                'is_featured' => $isFeatured,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete a product image
     *
     * @param string $productId
     * @param string $imageId
     * @return void
     */
    public function deleteImage(string $productId, string $imageId): void
    {
        $this->httpClient->delete("/api/products/{$productId}/images/{$imageId}");
    }
}
