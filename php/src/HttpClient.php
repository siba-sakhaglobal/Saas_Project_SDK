<?php

declare(strict_types=1);

namespace Sakha\CMS;

use GuzzleHttp\Client;
use GuzzleHttp\ClientInterface;
use GuzzleHttp\Exception\GuzzleException;
use Sakha\CMS\Exceptions\AuthException;
use Sakha\CMS\Exceptions\NotFoundException;
use Sakha\CMS\Exceptions\SakhaCMSException;
use Sakha\CMS\Exceptions\ValidationException;

/**
 * HTTP client wrapper for Sakha CMS API
 */
class HttpClient
{
    private ClientInterface $client;
    private string $baseUrl;
    private string $apiKey;
    private ?string $jwtToken = null;

    public function __construct(
        string $baseUrl,
        string $apiKey,
        ?ClientInterface $client = null
    ) {
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->apiKey = $apiKey;
        $this->client = $client ?? new Client([
            'base_uri' => $this->baseUrl,
            'timeout' => 30,
        ]);
    }

    /**
     * Set JWT token for end-user authenticated requests
     */
    public function setJwtToken(?string $token): void
    {
        $this->jwtToken = $token;
    }

    /**
     * Get current JWT token
     */
    public function getJwtToken(): ?string
    {
        return $this->jwtToken;
    }

    /**
     * Perform a GET request
     *
     * @param string $path API path (e.g., "/api/blog/posts")
     * @param array<string, mixed> $query Query parameters
     * @return array<string, mixed> Parsed response data
     * @throws SakhaCMSException
     */
    public function get(string $path, array $query = []): array
    {
        return $this->request('GET', $path, ['query' => $query]);
    }

    /**
     * Perform a POST request
     *
     * @param string $path API path
     * @param array<string, mixed> $data Request body
     * @return array<string, mixed> Parsed response data
     * @throws SakhaCMSException
     */
    public function post(string $path, array $data = []): array
    {
        return $this->request('POST', $path, ['json' => $data]);
    }

    /**
     * Perform a PUT request
     *
     * @param string $path API path
     * @param array<string, mixed> $data Request body
     * @return array<string, mixed> Parsed response data
     * @throws SakhaCMSException
     */
    public function put(string $path, array $data = []): array
    {
        return $this->request('PUT', $path, ['json' => $data]);
    }

    /**
     * Perform a PATCH request
     *
     * @param string $path API path
     * @param array<string, mixed> $data Request body
     * @return array<string, mixed> Parsed response data
     * @throws SakhaCMSException
     */
    public function patch(string $path, array $data = []): array
    {
        return $this->request('PATCH', $path, ['json' => $data]);
    }

    /**
     * Perform a DELETE request
     *
     * @param string $path API path
     * @return array<string, mixed> Parsed response data
     * @throws SakhaCMSException
     */
    public function delete(string $path): array
    {
        return $this->request('DELETE', $path);
    }

    /**
     * Perform an HTTP request with proper error handling
     *
     * @param string $method HTTP method
     * @param string $path API path
     * @param array<string, mixed> $options Guzzle request options
     * @return array<string, mixed> Parsed response data
     * @throws SakhaCMSException
     */
    private function request(string $method, string $path, array $options = []): array
    {
        try {
            // Build headers
            $headers = $this->buildHeaders();

            // Merge options
            $requestOptions = array_merge($options, ['headers' => $headers]);

            // Send request
            $response = $this->client->request($method, $path, $requestOptions);

            // Parse response
            $statusCode = $response->getStatusCode();
            $body = (string) $response->getBody();

            $data = json_decode($body, true, 512, JSON_THROW_ON_ERROR);

            // Validate response structure
            if (!is_array($data)) {
                throw new SakhaCMSException('Invalid API response format');
            }

            return $data;
        } catch (GuzzleException $e) {
            $this->handleGuzzleException($e);
        } catch (\JsonException $e) {
            throw new SakhaCMSException('Failed to parse API response: ' . $e->getMessage());
        }
    }

    /**
     * Build request headers with authentication
     *
     * @return array<string, string>
     */
    private function buildHeaders(): array
    {
        $headers = [
            'Content-Type' => 'application/json',
            'Accept' => 'application/json',
            'Authorization' => 'Bearer ' . $this->apiKey,
        ];

        if ($this->jwtToken) {
            $headers['X-User-Token'] = $this->jwtToken;
        }

        return $headers;
    }

    /**
     * Handle Guzzle exceptions and convert to SDK exceptions
     *
     * @throws SakhaCMSException
     * @throws NotFoundException
     * @throws ValidationException
     * @throws AuthException
     */
    private function handleGuzzleException(GuzzleException $e): void
    {
        $response = null;
        $statusCode = null;
        $responseData = null;

        if ($e instanceof \GuzzleHttp\Exception\ClientException ||
            $e instanceof \GuzzleHttp\Exception\ServerException) {
            $response = $e->getResponse();
            $statusCode = $response->getStatusCode();

            try {
                $body = (string) $response->getBody();
                $responseData = json_decode($body, true, 512, JSON_THROW_ON_ERROR);
            } catch (\Exception) {
                $responseData = null;
            }
        }

        $message = $e->getMessage();

        // Extract error message from response if available
        if ($responseData && isset($responseData['error'])) {
            $message = $responseData['error'];
        }

        // Throw appropriate exception based on status code
        match ($statusCode) {
            404 => throw new NotFoundException($message, $statusCode, $responseData),
            400 => throw new ValidationException($message, $statusCode, $responseData),
            401, 403 => throw new AuthException($message, $statusCode, $responseData),
            default => throw new SakhaCMSException($message, $statusCode, $responseData),
        };
    }
}
