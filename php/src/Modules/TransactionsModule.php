<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

use Sakha\CMS\Models\PaginatedResponse;

/**
 * Transactions module for managing project transactions
 * Base: /api/project-transactions
 */
class TransactionsModule extends BaseModule
{
    /**
     * List all transactions with pagination and filtering
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @param ?string $type Filter by type: payment, refund, adjustment
     * @param ?string $status Filter by status: pending, completed, failed, cancelled
     * @param ?string $customerId Filter by customer ID
     * @return PaginatedResponse
     */
    public function listTransactions(
        int $page = 1,
        int $limit = 50,
        ?string $type = null,
        ?string $status = null,
        ?string $customerId = null,
    ): PaginatedResponse {
        $response = $this->httpClient->get('/api/project-transactions', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
            'type' => $type,
            'status' => $status,
            'customer_id' => $customerId,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific transaction by ID
     *
     * @param string $transactionId
     * @return array<string, mixed>
     */
    public function getTransaction(string $transactionId): array
    {
        return $this->httpClient->get("/api/project-transactions/{$transactionId}")['data'] ?? [];
    }

    /**
     * Create a new transaction
     *
     * @param string $type Transaction type: payment, refund, adjustment
     * @param int $amountCents Amount in cents
     * @param string $status Transaction status
     * @param ?string $customerId Customer ID
     * @param ?string $orderId Order ID
     * @param ?string $invoiceId Invoice ID
     * @param ?string $paymentMethod Payment method
     * @param ?string $paymentGateway Payment gateway
     * @param ?string $reference Transaction reference/ID from gateway
     * @param ?array<string, mixed> $metadata Additional metadata
     * @return array<string, mixed>
     */
    public function createTransaction(
        string $type,
        int $amountCents,
        string $status = 'pending',
        ?string $customerId = null,
        ?string $orderId = null,
        ?string $invoiceId = null,
        ?string $paymentMethod = null,
        ?string $paymentGateway = null,
        ?string $reference = null,
        ?array $metadata = null,
    ): array {
        $response = $this->httpClient->post('/api/project-transactions', $this->buildQuery([
            'type' => $type,
            'amount_cents' => $amountCents,
            'status' => $status,
            'customer_id' => $customerId,
            'order_id' => $orderId,
            'invoice_id' => $invoiceId,
            'payment_method' => $paymentMethod,
            'payment_gateway' => $paymentGateway,
            'reference' => $reference,
            'metadata' => $metadata,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update a transaction
     *
     * @param string $transactionId
     * @param ?string $status
     * @param ?int $amountCents
     * @param ?string $paymentMethod
     * @param ?string $paymentGateway
     * @param ?string $reference
     * @param ?array<string, mixed> $metadata
     * @return array<string, mixed>
     */
    public function updateTransaction(
        string $transactionId,
        ?string $status = null,
        ?int $amountCents = null,
        ?string $paymentMethod = null,
        ?string $paymentGateway = null,
        ?string $reference = null,
        ?array $metadata = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/project-transactions/{$transactionId}",
            $this->buildQuery([
                'status' => $status,
                'amount_cents' => $amountCents,
                'payment_method' => $paymentMethod,
                'payment_gateway' => $paymentGateway,
                'reference' => $reference,
                'metadata' => $metadata,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete a transaction
     *
     * @param string $transactionId
     * @return void
     */
    public function deleteTransaction(string $transactionId): void
    {
        $this->httpClient->delete("/api/project-transactions/{$transactionId}");
    }
}
