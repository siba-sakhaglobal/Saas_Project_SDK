"""Sakha CMS client."""

from .client import HttpClient
from .modules import (
    BlogModule,
    EventsModule,
    DonationsModule,
    OrdersModule,
    InvoicesModule,
    TransactionsModule,
    ServicesModule,
    AppointmentsModule,
    VendorsModule,
    BannersModule,
    ShipmentsModule,
    ProductsModule,
    TeamModule,
    UsersModule,
    MediaModule,
    AnalyticsModule,
    UserGroupsModule,
)


class SakhaCMS:
    """Sakha CMS client."""

    def __init__(
        self,
        base_url: str,
        api_key: str,
        api_secret: str | None = None,
        jwt_token: str | None = None,
        timeout: int = 30,
    ) -> None:
        """Initialize Sakha CMS client.

        Args:
            base_url: Base URL for API (e.g., 'https://api.example.com')
            api_key: API key for authentication
            api_secret: API secret for authentication (optional)
            jwt_token: End-user JWT token (optional)
            timeout: Request timeout in seconds
        """
        self._client = HttpClient(
            base_url=base_url,
            api_key=api_key,
            api_secret=api_secret,
            jwt_token=jwt_token,
            timeout=timeout,
        )

        self.blog = BlogModule(self._client)
        self.events = EventsModule(self._client)
        self.donations = DonationsModule(self._client)
        self.orders = OrdersModule(self._client)
        self.invoices = InvoicesModule(self._client)
        self.transactions = TransactionsModule(self._client)
        self.services = ServicesModule(self._client)
        self.appointments = AppointmentsModule(self._client)
        self.vendors = VendorsModule(self._client)
        self.banners = BannersModule(self._client)
        self.shipments = ShipmentsModule(self._client)
        self.products = ProductsModule(self._client)
        self.team = TeamModule(self._client)
        self.users = UsersModule(self._client)
        self.media = MediaModule(self._client)
        self.analytics = AnalyticsModule(self._client)
        self.user_groups = UserGroupsModule(self._client)

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    async def close_async(self) -> None:
        """Close the async HTTP client."""
        await self._client.close_async()
