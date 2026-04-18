"""Donations module models."""

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class DonationCampaign(BaseModel):
    """Donation campaign."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    description: Optional[str] = None
    goal_amount: float = Field(alias="goal_amount")
    raised_amount: float = Field(alias="raised_amount")
    donors_count: Optional[int] = Field(None, alias="donors_count")
    category: Optional[str] = None
    status: str  # active|paused|completed
    image_url: Optional[str] = Field(None, alias="image_url")
    start_date: datetime = Field(alias="start_date")
    end_date: Optional[datetime] = Field(None, alias="end_date")
    progress: int
    created_at: datetime = Field(alias="created_at")
    updated_at: datetime = Field(alias="updated_at")


class Donation(BaseModel):
    """Donation."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    campaign_id: str = Field(alias="campaign_id")
    donor_name: Optional[str] = Field(None, alias="donor_name")
    donor_email: Optional[str] = Field(None, alias="donor_email")
    amount: float
    payment_ref: Optional[str] = Field(None, alias="payment_ref")
    created_at: datetime = Field(alias="created_at")


class CreateDonationCampaignBody(BaseModel):
    """Create donation campaign request."""

    model_config = ConfigDict(populate_by_name=True)

    title: str
    description: Optional[str] = None
    goal_cents: int = Field(alias="goalCents")
    raised_cents: Optional[int] = Field(None, alias="raisedCents")
    donor_count: Optional[int] = Field(None, alias="donorCount")
    status: str = "active"
    cover_image: Optional[str] = Field(None, alias="coverImage")
    start_date: datetime = Field(alias="startDate")
    end_date: Optional[datetime] = Field(None, alias="endDate")


class UpdateDonationCampaignBody(BaseModel):
    """Update donation campaign request."""

    model_config = ConfigDict(populate_by_name=True)

    title: Optional[str] = None
    description: Optional[str] = None
    goal_cents: Optional[int] = Field(None, alias="goalCents")
    raised_cents: Optional[int] = Field(None, alias="raisedCents")
    donor_count: Optional[int] = Field(None, alias="donorCount")
    status: Optional[str] = None
    cover_image: Optional[str] = Field(None, alias="coverImage")
    start_date: Optional[datetime] = Field(None, alias="startDate")
    end_date: Optional[datetime] = Field(None, alias="endDate")


class DonationStats(BaseModel):
    """Donation statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total_campaigns: int = Field(alias="totalCampaigns")
    active_campaigns: int = Field(alias="activeCampaigns")
    total_raised: float = Field(alias="totalRaised")
    total_donors: int = Field(alias="totalDonors")
    this_month_donations: float = Field(alias="thisMonthDonations")
    average_donation: float = Field(alias="averageDonation")
