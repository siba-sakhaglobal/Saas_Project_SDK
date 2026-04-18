"""Exception classes for Sakha CMS SDK."""


class SakhaCMSError(Exception):
    """Base exception for all Sakha CMS SDK errors."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class AuthError(SakhaCMSError):
    """Raised when authentication fails (401)."""

    pass


class NotFoundError(SakhaCMSError):
    """Raised when a resource is not found (404)."""

    def __init__(self, resource: str, message: str | None = None) -> None:
        self.resource = resource
        final_message = message or f"{resource} not found"
        super().__init__(final_message)


class ValidationError(SakhaCMSError):
    """Raised when validation fails (400)."""

    def __init__(self, message: str, details: dict[str, list[str]] | None = None) -> None:
        self.details = details or {}
        super().__init__(message)


class PermissionError(SakhaCMSError):
    """Raised when user lacks required permissions (403)."""

    pass


class ServerError(SakhaCMSError):
    """Raised when server returns a 5xx error."""

    def __init__(self, message: str, status_code: int) -> None:
        self.status_code = status_code
        super().__init__(message)
