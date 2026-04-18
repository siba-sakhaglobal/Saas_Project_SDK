"""Analytics module models."""

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class PageView(BaseModel):
    """Page view."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    project_id: Optional[str] = Field(None, alias="project_id")
    page_url: str = Field(alias="page_url")
    user_agent: Optional[str] = Field(None, alias="user_agent")
    ip_address: Optional[str] = Field(None, alias="ip_address")
    referrer: Optional[str] = None
    session_id: Optional[str] = Field(None, alias="session_id")


class AnalyticsStats(BaseModel):
    """Analytics statistics."""

    model_config = ConfigDict(populate_by_name=True)

    total_views: int = Field(alias="totalViews")
    unique_visitors: int = Field(alias="uniqueVisitors")
    total_sessions: int = Field(alias="totalSessions")
    bounce_rate: float = Field(alias="bounceRate")
    average_session_duration: float = Field(alias="averageSessionDuration")
    top_pages: list[dict] = Field(default_factory=list, alias="topPages")
    top_referrers: list[dict] = Field(default_factory=list, alias="topReferrers")
    device_stats: dict = Field(default_factory=dict, alias="deviceStats")
    browser_stats: dict = Field(default_factory=dict, alias="browserStats")


class TrafficStats(BaseModel):
    """Traffic statistics."""

    model_config = ConfigDict(populate_by_name=True)

    date: str
    views: int
    unique_visitors: int = Field(alias="uniqueVisitors")
    sessions: int
    bounce_rate: float = Field(alias="bounceRate")
