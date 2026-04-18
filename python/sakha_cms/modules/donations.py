"""Donations module client."""

from typing import Optional
from ..client import HttpClient
from ..models import (
    DonationCampaign,
    Donation,
    DonationStats,
    CreateDonationCampaignBody,
    UpdateDonationCampaignBody,
    PaginatedResponse,
)


class DonationsModule:
    """Donations module client."""

    def __init__(self, client: HttpClient) -> None:
        """Initialize donations module.

        Args:
            client: HTTP client instance
        """
        self.client = client

    # Donation Campaigns
    def get_campaigns(
        self,
        limit: int = 50,
        page: int = 1,
        search: Optional[str] = None,
    ) -> PaginatedResponse[DonationCampaign]:
        """Get all donation campaigns.

        Args:
            limit: Items per page
            page: Page number
            search: Search query

        Returns:
            Paginated donation campaigns
        """
        data = self.client.get(
            "/api/donations/campaigns",
            limit=limit,
            page=page,
            search=search,
        )
        return self._parse_paginated_response(data, DonationCampaign)

    async def get_campaigns_async(
        self,
        limit: int = 50,
        page: int = 1,
        search: Optional[str] = None,
    ) -> PaginatedResponse[DonationCampaign]:
        """Get all donation campaigns (async).

        Args:
            limit: Items per page
            page: Page number
            search: Search query

        Returns:
            Paginated donation campaigns
        """
        data = await self.client.get_async(
            "/api/donations/campaigns",
            limit=limit,
            page=page,
            search=search,
        )
        return self._parse_paginated_response(data, DonationCampaign)

    def get_campaign(self, campaign_id: str) -> DonationCampaign:
        """Get a donation campaign by ID.

        Args:
            campaign_id: Campaign ID

        Returns:
            Donation campaign
        """
        data = self.client.get(f"/api/donations/campaigns/{campaign_id}")
        return DonationCampaign(**data)

    async def get_campaign_async(self, campaign_id: str) -> DonationCampaign:
        """Get a donation campaign by ID (async).

        Args:
            campaign_id: Campaign ID

        Returns:
            Donation campaign
        """
        data = await self.client.get_async(f"/api/donations/campaigns/{campaign_id}")
        return DonationCampaign(**data)

    def create_campaign(self, body: CreateDonationCampaignBody) -> DonationCampaign:
        """Create a donation campaign.

        Args:
            body: Create campaign request

        Returns:
            Created donation campaign
        """
        data = self.client.post(
            "/api/donations/campaigns",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return DonationCampaign(**data)

    async def create_campaign_async(self, body: CreateDonationCampaignBody) -> DonationCampaign:
        """Create a donation campaign (async).

        Args:
            body: Create campaign request

        Returns:
            Created donation campaign
        """
        data = await self.client.post_async(
            "/api/donations/campaigns",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return DonationCampaign(**data)

    def update_campaign(self, campaign_id: str, body: UpdateDonationCampaignBody) -> DonationCampaign:
        """Update a donation campaign.

        Args:
            campaign_id: Campaign ID
            body: Update campaign request

        Returns:
            Updated donation campaign
        """
        data = self.client.put(
            f"/api/donations/campaigns/{campaign_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return DonationCampaign(**data)

    async def update_campaign_async(
        self, campaign_id: str, body: UpdateDonationCampaignBody
    ) -> DonationCampaign:
        """Update a donation campaign (async).

        Args:
            campaign_id: Campaign ID
            body: Update campaign request

        Returns:
            Updated donation campaign
        """
        data = await self.client.put_async(
            f"/api/donations/campaigns/{campaign_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return DonationCampaign(**data)

    def delete_campaign(self, campaign_id: str) -> None:
        """Delete a donation campaign.

        Args:
            campaign_id: Campaign ID
        """
        self.client.delete(f"/api/donations/campaigns/{campaign_id}")

    async def delete_campaign_async(self, campaign_id: str) -> None:
        """Delete a donation campaign (async).

        Args:
            campaign_id: Campaign ID
        """
        await self.client.delete_async(f"/api/donations/campaigns/{campaign_id}")

    # Donations
    def get_donations(
        self,
        limit: int = 50,
        page: int = 1,
    ) -> PaginatedResponse[Donation]:
        """Get all donations.

        Args:
            limit: Items per page
            page: Page number

        Returns:
            Paginated donations
        """
        data = self.client.get(
            "/api/donations/donations",
            limit=limit,
            page=page,
        )
        return self._parse_paginated_response(data, Donation)

    async def get_donations_async(
        self,
        limit: int = 50,
        page: int = 1,
    ) -> PaginatedResponse[Donation]:
        """Get all donations (async).

        Args:
            limit: Items per page
            page: Page number

        Returns:
            Paginated donations
        """
        data = await self.client.get_async(
            "/api/donations/donations",
            limit=limit,
            page=page,
        )
        return self._parse_paginated_response(data, Donation)

    def get_donation(self, donation_id: str) -> Donation:
        """Get a donation by ID.

        Args:
            donation_id: Donation ID

        Returns:
            Donation
        """
        data = self.client.get(f"/api/donations/donations/{donation_id}")
        return Donation(**data)

    async def get_donation_async(self, donation_id: str) -> Donation:
        """Get a donation by ID (async).

        Args:
            donation_id: Donation ID

        Returns:
            Donation
        """
        data = await self.client.get_async(f"/api/donations/donations/{donation_id}")
        return Donation(**data)

    # Donation Stats
    def get_stats(self) -> DonationStats:
        """Get donation statistics.

        Returns:
            Donation statistics
        """
        data = self.client.get("/api/donations/stats/overview")
        return DonationStats(**data)

    async def get_stats_async(self) -> DonationStats:
        """Get donation statistics (async).

        Returns:
            Donation statistics
        """
        data = await self.client.get_async("/api/donations/stats/overview")
        return DonationStats(**data)

    @staticmethod
    def _parse_paginated_response(data: dict, model: type) -> PaginatedResponse:
        """Parse paginated response."""
        if isinstance(data, dict) and "items" in data:
            items = [model(**item) for item in data.get("items", [])]
            meta = data.get("meta", {})
            return PaginatedResponse(items=items, meta=meta)
        return PaginatedResponse(items=[], meta={"total": 0, "page": 1, "limit": 50})
