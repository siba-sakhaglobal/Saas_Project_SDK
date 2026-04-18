<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

use Sakha\CMS\Models\PaginatedResponse;

/**
 * Orders module for managing project orders
 * Base: /api/project-orders
 */
class OrdersModule extends BaseModule
{
    /**
     * List all orders with pagination and filtering
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @param ?string $status Filter by status: pending, confirmed, shipped, delivered, cancelled
     * @param ?string $customerId Filter by customer ID
     * @param ?string $search Search by order number
     * @return PaginatedResponse
     */
    public function listOrders(
        int $page = 1,
        int $limit = 50,
        ?string $status = null,
        ?string $customerId = null,
        ?string $search = null,
    ): PaginatedResponse {
        $response = $this->httpClient->get('/api/project-orders', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
            'status' => $status,
            'customer_id' => $customerId,
            'search' => $search,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific order by ID
     *
     * @param string $orderId
     * @return array<string, mixed>
     */
    public function getOrder(string $orderId): array
    {
        return $this->httpClient->get("/api/project-orders/{$orderId}")['data'] ?? [];
    }

    /**
     * Create a new order
     *
     * @param string $customerId Customer ID
     * @param array<array<string, mixed>> $items Order items (product_id, quantity, price_cents)
     * @param int $totalAmountCents Total amount in cents
     * @param string $status Order status
     * @param ?string $shippingAddress Shipping address
     * @param ?string $billingAddress Billing address
     * @param ?array<string, mixed> $metadata Additional metadata
     * @return array<string, mixed>
     */
    public function createOrder(
        string $customerId,
        array $items,
        int $totalAmountCents,
        string $status = 'pending',
        ?string $shippingAddress = null,
        ?string $billingAddress = null,
        ?array $metadata = null,
    ): array {
        $response = $this->httpClient->post('/api/project-orders', $this->buildQuery([
            'customer_id' => $customerId,
            'items' => $items,
            'total_amount_cents' => $totalAmountCents,
            'status' => $status,
            'shipping_address' => $shippingAddress,
            'billing_address' => $billingAddress,
            'metadata' => $metadata,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update an order
     *
     * @param string $orderId
     * @param ?string $status
     * @param ?array<array<string, mixed>> $items
     * @param ?int $totalAmountCents
     * @param ?string $shippingAddress
     * @param ?string $billingAddress
     * @param ?array<string, mixed> $metadata
     * @return array<string, mixed>
     */
    public function updateOrder(
        string $orderId,
        ?string $status = null,
        ?array $items = null,
        ?int $totalAmountCents = null,
        ?string $shippingAddress = null,
        ?string $billingAddress = null,
        ?array $metadata = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/project-orders/{$orderId}",
            $this->buildQuery([
                'status' => $status,
                'items' => $items,
                'total_amount_cents' => $totalAmountCents,
                'shipping_address' => $shippingAddress,
                'billing_address' => $billingAddress,
                'metadata' => $metadata,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete an order
     *
     * @param string $orderId
     * @return void
     */
    public function deleteOrder(string $orderId): void
    {
        $this->httpClient->delete("/api/project-orders/{$orderId}");
    }
}
