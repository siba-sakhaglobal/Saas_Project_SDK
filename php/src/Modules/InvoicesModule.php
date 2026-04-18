<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

use Sakha\CMS\Models\PaginatedResponse;

/**
 * Invoices module for managing project invoices
 * Base: /api/project-invoices
 */
class InvoicesModule extends BaseModule
{
    /**
     * List all invoices with pagination and filtering
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @param ?string $status Filter by status: draft, sent, paid, overdue, cancelled
     * @param ?string $customerId Filter by customer ID
     * @param ?string $search Search by invoice number
     * @return PaginatedResponse
     */
    public function listInvoices(
        int $page = 1,
        int $limit = 50,
        ?string $status = null,
        ?string $customerId = null,
        ?string $search = null,
    ): PaginatedResponse {
        $response = $this->httpClient->get('/api/project-invoices', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
            'status' => $status,
            'customer_id' => $customerId,
            'search' => $search,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific invoice by ID
     *
     * @param string $invoiceId
     * @return array<string, mixed>
     */
    public function getInvoice(string $invoiceId): array
    {
        return $this->httpClient->get("/api/project-invoices/{$invoiceId}")['data'] ?? [];
    }

    /**
     * Create a new invoice
     *
     * @param string $customerId Customer ID
     * @param array<array<string, mixed>> $lineItems Invoice line items (description, quantity, unit_price_cents)
     * @param int $amountCents Invoice amount in cents
     * @param string $status Invoice status
     * @param ?string $dueDate Due date (ISO 8601)
     * @param ?string $notes Invoice notes
     * @param ?array<string, mixed> $metadata Additional metadata
     * @return array<string, mixed>
     */
    public function createInvoice(
        string $customerId,
        array $lineItems,
        int $amountCents,
        string $status = 'draft',
        ?string $dueDate = null,
        ?string $notes = null,
        ?array $metadata = null,
    ): array {
        $response = $this->httpClient->post('/api/project-invoices', $this->buildQuery([
            'customer_id' => $customerId,
            'line_items' => $lineItems,
            'amount_cents' => $amountCents,
            'status' => $status,
            'due_date' => $dueDate,
            'notes' => $notes,
            'metadata' => $metadata,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update an invoice
     *
     * @param string $invoiceId
     * @param ?string $status
     * @param ?array<array<string, mixed>> $lineItems
     * @param ?int $amountCents
     * @param ?string $dueDate
     * @param ?string $notes
     * @param ?array<string, mixed> $metadata
     * @return array<string, mixed>
     */
    public function updateInvoice(
        string $invoiceId,
        ?string $status = null,
        ?array $lineItems = null,
        ?int $amountCents = null,
        ?string $dueDate = null,
        ?string $notes = null,
        ?array $metadata = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/project-invoices/{$invoiceId}",
            $this->buildQuery([
                'status' => $status,
                'line_items' => $lineItems,
                'amount_cents' => $amountCents,
                'due_date' => $dueDate,
                'notes' => $notes,
                'metadata' => $metadata,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete an invoice
     *
     * @param string $invoiceId
     * @return void
     */
    public function deleteInvoice(string $invoiceId): void
    {
        $this->httpClient->delete("/api/project-invoices/{$invoiceId}");
    }

    /**
     * Send an invoice to customer
     *
     * @param string $invoiceId
     * @param string $recipientEmail Email address to send to
     * @return array<string, mixed>
     */
    public function sendInvoice(string $invoiceId, string $recipientEmail): array
    {
        $response = $this->httpClient->post(
            "/api/project-invoices/{$invoiceId}/send",
            ['recipient_email' => $recipientEmail],
        );

        return $response['data'] ?? [];
    }
}
