<?php

declare(strict_types=1);

namespace Sakha\CMS\Modules;

/**
 * End Users module for public end-user authentication (register/login/me/logout)
 * Base: /api/v1/users
 */
class EndUsersModule extends BaseModule
{
    /**
     * Get signup form schema for this project
     *
     * @return array<int, array<string, mixed>> Array of signup field definitions
     */
    public function getSignupFields(): array
    {
        return $this->httpClient->get('/api/v1/users/signup-fields')['data'] ?? [];
    }

    /**
     * Register a new end user
     *
     * @param string $email User email
     * @param string $password Password (min 8 chars)
     * @param ?string $fullName User full name
     * @param ?string $phone User phone
     * @param array<string, mixed> $customFields Additional custom fields from signup schema
     * @return array<string, mixed> Contains endUser, accessToken, refreshToken
     */
    public function register(
        string $email,
        string $password,
        ?string $fullName = null,
        ?string $phone = null,
        array $customFields = [],
    ): array {
        $payload = [
            'email' => $email,
            'password' => $password,
        ];

        if ($fullName !== null) {
            $payload['full_name'] = $fullName;
        }

        if ($phone !== null) {
            $payload['phone'] = $phone;
        }

        // Add custom fields
        foreach ($customFields as $key => $value) {
            $payload[$key] = $value;
        }

        $response = $this->httpClient->post('/api/v1/users/register', $payload);

        // Store access token if successful
        if (isset($response['data']['accessToken'])) {
            $this->httpClient->setJwtToken($response['data']['accessToken']);
        }

        return $response['data'] ?? [];
    }

    /**
     * Login an end user
     *
     * @param string $email User email
     * @param string $password User password
     * @return array<string, mixed> Contains endUser, accessToken, refreshToken
     */
    public function login(string $email, string $password): array
    {
        $response = $this->httpClient->post('/api/v1/users/login', [
            'email' => $email,
            'password' => $password,
        ]);

        // Store access token if successful
        if (isset($response['data']['accessToken'])) {
            $this->httpClient->setJwtToken($response['data']['accessToken']);
        }

        return $response['data'] ?? [];
    }

    /**
     * Refresh an expired access token
     *
     * @param string $refreshToken
     * @return array<string, mixed> Contains new accessToken
     */
    public function refresh(string $refreshToken): array
    {
        $response = $this->httpClient->post('/api/v1/users/refresh', [
            'refreshToken' => $refreshToken,
        ]);

        // Update access token if successful
        if (isset($response['data']['accessToken'])) {
            $this->httpClient->setJwtToken($response['data']['accessToken']);
        }

        return $response['data'] ?? [];
    }

    /**
     * Get current end-user profile (requires JWT)
     *
     * @return array<string, mixed> User profile data
     */
    public function getProfile(): array
    {
        return $this->httpClient->get('/api/v1/users/me')['data'] ?? [];
    }

    /**
     * Logout current end user (revokes all sessions)
     *
     * @return void
     */
    public function logout(): void
    {
        $this->httpClient->post('/api/v1/users/logout', []);
        // Clear JWT token
        $this->httpClient->setJwtToken(null);
    }
}
