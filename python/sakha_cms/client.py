"""HTTP client with authentication and error handling."""

import base64
import httpx
from typing import Any

from .exceptions import (
    AuthError,
    NotFoundError,
    ValidationError,
    PermissionError,
    ServerError,
    SakhaCMSError,
)


class HttpClient:
    """HTTP client with authentication and error handling."""

    def __init__(
        self,
        base_url: str,
        api_key: str,
        api_secret: str | None = None,
        jwt_token: str | None = None,
        timeout: int = 30,
    ) -> None:
        """Initialize HTTP client.

        Args:
            base_url: Base URL for API (e.g., 'https://api.example.com')
            api_key: API key for authentication
            api_secret: API secret for authentication (optional)
            jwt_token: End-user JWT token (optional)
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.api_secret = api_secret
        self.jwt_token = jwt_token
        self.timeout = timeout
        self._client: httpx.Client | None = None
        self._async_client: httpx.AsyncClient | None = None

    def _get_auth_header(self) -> dict[str, str]:
        """Get authorization header based on auth mode."""
        if self.jwt_token:
            return {
                "Authorization": f"Bearer {self.jwt_token}",
                "X-Api-Key": self.api_key,
            }
        elif self.api_secret:
            return {"Authorization": f"Bearer {self.api_key}:{self.api_secret}"}
        else:
            return {"Authorization": f"Bearer {self.api_key}"}

    def _get_client(self) -> httpx.Client:
        """Get or create sync HTTP client."""
        if self._client is None:
            self._client = httpx.Client(
                base_url=self.base_url,
                timeout=self.timeout,
                headers=self._get_auth_header(),
            )
        return self._client

    def _get_async_client(self) -> httpx.AsyncClient:
        """Get or create async HTTP client."""
        if self._async_client is None:
            self._async_client = httpx.AsyncClient(
                base_url=self.base_url,
                timeout=self.timeout,
                headers=self._get_auth_header(),
            )
        return self._async_client

    def _handle_response(self, response: httpx.Response) -> Any:
        """Handle response and raise appropriate exceptions."""
        if 400 <= response.status_code < 500:
            self._handle_client_error(response)
        elif response.status_code >= 500:
            raise ServerError(
                f"Server error: {response.text}",
                response.status_code,
            )

        if response.status_code == 204:
            return None

        try:
            data = response.json()
        except httpx.ResponseNotRead:
            return None

        if isinstance(data, dict) and "data" in data:
            return data["data"]
        return data

    def _handle_client_error(self, response: httpx.Response) -> None:
        """Handle 4xx client errors."""
        try:
            error_data = response.json()
        except (httpx.ResponseNotRead, ValueError):
            error_data = {}

        if response.status_code == 401:
            raise AuthError("Unauthorized: invalid credentials or expired token")

        if response.status_code == 403:
            raise PermissionError("Forbidden: insufficient permissions")

        if response.status_code == 404:
            error_msg = error_data.get("error", "Resource not found")
            if isinstance(error_msg, str):
                raise NotFoundError("resource", error_msg)
            raise NotFoundError("resource")

        if response.status_code == 400:
            error = error_data.get("error", {})
            if isinstance(error, dict):
                raise ValidationError("Validation failed", error)
            raise ValidationError(str(error))

        raise SakhaCMSError(f"HTTP {response.status_code}: {response.text}")

    def get(self, path: str, **params: Any) -> Any:
        """Make GET request."""
        response = self._get_client().get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        return self._handle_response(response)

    def post(self, path: str, json: dict[str, Any] | None = None, **params: Any) -> Any:
        """Make POST request."""
        response = self._get_client().post(
            path,
            json=json,
            params={k: v for k, v in params.items() if v is not None},
        )
        return self._handle_response(response)

    def put(self, path: str, json: dict[str, Any] | None = None, **params: Any) -> Any:
        """Make PUT request."""
        response = self._get_client().put(
            path,
            json=json,
            params={k: v for k, v in params.items() if v is not None},
        )
        return self._handle_response(response)

    def delete(self, path: str, **params: Any) -> Any:
        """Make DELETE request."""
        response = self._get_client().delete(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        return self._handle_response(response)

    async def get_async(self, path: str, **params: Any) -> Any:
        """Make async GET request."""
        response = await self._get_async_client().get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        return self._handle_response(response)

    async def post_async(
        self, path: str, json: dict[str, Any] | None = None, **params: Any
    ) -> Any:
        """Make async POST request."""
        response = await self._get_async_client().post(
            path,
            json=json,
            params={k: v for k, v in params.items() if v is not None},
        )
        return self._handle_response(response)

    async def put_async(
        self, path: str, json: dict[str, Any] | None = None, **params: Any
    ) -> Any:
        """Make async PUT request."""
        response = await self._get_async_client().put(
            path,
            json=json,
            params={k: v for k, v in params.items() if v is not None},
        )
        return self._handle_response(response)

    async def delete_async(self, path: str, **params: Any) -> Any:
        """Make async DELETE request."""
        response = await self._get_async_client().delete(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        return self._handle_response(response)

    def close(self) -> None:
        """Close sync client."""
        if self._client:
            self._client.close()

    async def close_async(self) -> None:
        """Close async client."""
        if self._async_client:
            await self._async_client.aclose()
