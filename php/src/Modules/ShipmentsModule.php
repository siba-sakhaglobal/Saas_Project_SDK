<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

use Sakha\CMS\Models\PaginatedResponse;

/**
 * Shipments module for managing project shipments
 * Base: /api/project-shipments
 */
class ShipmentsModule extends BaseModule
{
    /**
     * List all shipments with pagination and filtering
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @param ?string $status Filter by status: pending, in_transit, delivered, cancelled
     * @param ?string $orderId Filter by order ID
     * @param ?string $search Search by tracking number
     * @return PaginatedResponse
     */
    public function listShipments(
        int $page = 1,
        int $limit = 50,
        ?string $status = null,
        ?string $orderId = null,
        ?string $search = null,
    ): PaginatedResponse {
        $response = $this->httpClient->get('/api/project-shipments', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
            'status' => $status,
            'order_id' => $orderId,
            'search' => $search,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific shipment by ID
     *
     * @param string $shipmentId
     * @return array<string, mixed>
     */
    public function getShipment(string $shipmentId): array
    {
        return $this->httpClient->get("/api/project-shipments/{$shipmentId}")['data'] ?? [];
    }

    /**
     * Create a new shipment
     *
     * @param string $orderId Order ID
     * @param string $carrier Shipping carrier (e.g., FedEx, UPS, DHL)
     * @param string $trackingNumber Tracking number
     * @param string $status Shipment status
     * @param ?string $shippingAddress Shipping address
     * @param ?string $estimatedDeliveryDate Estimated delivery date (ISO 8601)
     * @param ?array<string, mixed> $metadata Additional metadata
     * @return array<string, mixed>
     */
    public function createShipment(
        string $orderId,
        string $carrier,
        string $trackingNumber,
        string $status = 'pending',
        ?string $shippingAddress = null,
        ?string $estimatedDeliveryDate = null,
        ?array $metadata = null,
    ): array {
        $response = $this->httpClient->post('/api/project-shipments', $this->buildQuery([
            'order_id' => $orderId,
            'carrier' => $carrier,
            'tracking_number' => $trackingNumber,
            'status' => $status,
            'shipping_address' => $shippingAddress,
            'estimated_delivery_date' => $estimatedDeliveryDate,
            'metadata' => $metadata,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update a shipment
     *
     * @param string $shipmentId
     * @param ?string $status
     * @param ?string $carrier
     * @param ?string $trackingNumber
     * @param ?string $shippingAddress
     * @param ?string $estimatedDeliveryDate
     * @param ?array<string, mixed> $metadata
     * @return array<string, mixed>
     */
    public function updateShipment(
        string $shipmentId,
        ?string $status = null,
        ?string $carrier = null,
        ?string $trackingNumber = null,
        ?string $shippingAddress = null,
        ?string $estimatedDeliveryDate = null,
        ?array $metadata = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/project-shipments/{$shipmentId}",
            $this->buildQuery([
                'status' => $status,
                'carrier' => $carrier,
                'tracking_number' => $trackingNumber,
                'shipping_address' => $shippingAddress,
                'estimated_delivery_date' => $estimatedDeliveryDate,
                'metadata' => $metadata,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete a shipment
     *
     * @param string $shipmentId
     * @return void
     */
    public function deleteShipment(string $shipmentId): void
    {
        $this->httpClient->delete("/api/project-shipments/{$shipmentId}");
    }
}
