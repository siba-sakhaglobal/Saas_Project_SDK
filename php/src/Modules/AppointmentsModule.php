<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

use Sakha\CMS\Models\PaginatedResponse;

/**
 * Appointments module for managing project appointments
 * Base: /api/project-appointments
 */
class AppointmentsModule extends BaseModule
{
    /**
     * List all appointments with pagination and filtering
     *
     * @param int $page Page number (default: 1)
     * @param int $limit Items per page (default: 50)
     * @param ?string $status Filter by status: pending, confirmed, completed, cancelled
     * @param ?string $serviceId Filter by service ID
     * @param ?string $customerId Filter by customer ID
     * @param ?string $dateFrom Filter by start date (ISO 8601)
     * @param ?string $dateTo Filter by end date (ISO 8601)
     * @return PaginatedResponse
     */
    public function listAppointments(
        int $page = 1,
        int $limit = 50,
        ?string $status = null,
        ?string $serviceId = null,
        ?string $customerId = null,
        ?string $dateFrom = null,
        ?string $dateTo = null,
    ): PaginatedResponse {
        $response = $this->httpClient->get('/api/project-appointments', $this->buildQuery([
            'page' => $page,
            'limit' => $limit,
            'status' => $status,
            'service_id' => $serviceId,
            'customer_id' => $customerId,
            'date_from' => $dateFrom,
            'date_to' => $dateTo,
        ]));

        return $this->parsePaginatedResponse($response);
    }

    /**
     * Get a specific appointment by ID
     *
     * @param string $appointmentId
     * @return array<string, mixed>
     */
    public function getAppointment(string $appointmentId): array
    {
        return $this->httpClient->get("/api/project-appointments/{$appointmentId}")['data'] ?? [];
    }

    /**
     * Create a new appointment
     *
     * @param string $serviceId Service ID
     * @param string $customerId Customer ID
     * @param string $startDate Start date/time (ISO 8601)
     * @param string $endDate End date/time (ISO 8601)
     * @param string $status Appointment status
     * @param ?string $notes Appointment notes
     * @param ?array<string, mixed> $metadata Additional metadata
     * @return array<string, mixed>
     */
    public function createAppointment(
        string $serviceId,
        string $customerId,
        string $startDate,
        string $endDate,
        string $status = 'pending',
        ?string $notes = null,
        ?array $metadata = null,
    ): array {
        $response = $this->httpClient->post('/api/project-appointments', $this->buildQuery([
            'service_id' => $serviceId,
            'customer_id' => $customerId,
            'start_date' => $startDate,
            'end_date' => $endDate,
            'status' => $status,
            'notes' => $notes,
            'metadata' => $metadata,
        ]));

        return $response['data'] ?? [];
    }

    /**
     * Update an appointment
     *
     * @param string $appointmentId
     * @param ?string $status
     * @param ?string $startDate
     * @param ?string $endDate
     * @param ?string $notes
     * @param ?array<string, mixed> $metadata
     * @return array<string, mixed>
     */
    public function updateAppointment(
        string $appointmentId,
        ?string $status = null,
        ?string $startDate = null,
        ?string $endDate = null,
        ?string $notes = null,
        ?array $metadata = null,
    ): array {
        $response = $this->httpClient->put(
            "/api/project-appointments/{$appointmentId}",
            $this->buildQuery([
                'status' => $status,
                'start_date' => $startDate,
                'end_date' => $endDate,
                'notes' => $notes,
                'metadata' => $metadata,
            ]),
        );

        return $response['data'] ?? [];
    }

    /**
     * Delete an appointment
     *
     * @param string $appointmentId
     * @return void
     */
    public function deleteAppointment(string $appointmentId): void
    {
        $this->httpClient->delete("/api/project-appointments/{$appointmentId}");
    }
}
