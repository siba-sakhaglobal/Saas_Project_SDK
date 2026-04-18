<?php

declare(strict_types=1);

namespace Sakha\CMS\Exceptions;

use Exception;

/**
 * Base exception class for Sakha CMS SDK
 */
class SakhaCMSException extends Exception
{
    /**
     * HTTP status code from the API response
     */
    protected ?int $statusCode = null;

    /**
     * Error response from the API
     */
    protected ?array $responseData = null;

    public function __construct(
        string $message = '',
        ?int $statusCode = null,
        ?array $responseData = null,
        ?Exception $previous = null
    ) {
        parent::__construct($message, 0, $previous);
        $this->statusCode = $statusCode;
        $this->responseData = $responseData;
    }

    public function getStatusCode(): ?int
    {
        return $this->statusCode;
    }

    public function getResponseData(): ?array
    {
        return $this->responseData;
    }
}
