"""Sakha CMS models package."""

from .common import ApiResponse, ListParams, PaginatedMeta, PaginatedResponse
from .blog import (
    BlogAuthor,
    BlogCategory,
    BlogPost,
    CreateBlogPostBody,
    UpdateBlogPostBody,
    CreateBlogCategoryBody,
    UpdateBlogCategoryBody,
    BlogAuthorResponse,
    BlogStats,
)
from .events import (
    EventCategory,
    Event,
    CreateEventBody,
    UpdateEventBody,
    CreateEventCategoryBody,
    UpdateEventCategoryBody,
    EventStats,
)
from .donations import (
    DonationCampaign,
    Donation,
    CreateDonationCampaignBody,
    UpdateDonationCampaignBody,
    DonationStats,
)
from .orders import Order, OrderItem, CreateOrderBody, UpdateOrderBody, OrderStats
from .invoices import Invoice, InvoiceItem, CreateInvoiceBody, UpdateInvoiceBody, InvoiceStats
from .transactions import (
    Transaction,
    CreateTransactionBody,
    UpdateTransactionBody,
    TransactionStats,
)
from .services import Service, CreateServiceBody, UpdateServiceBody, ServiceStats
from .appointments import (
    Appointment,
    CreateAppointmentBody,
    UpdateAppointmentBody,
    AppointmentStats,
)
from .vendors import Vendor, CreateVendorBody, UpdateVendorBody, VendorStats
from .banners import Banner, CreateBannerBody, UpdateBannerBody, BannerStats
from .shipments import Shipment, CreateShipmentBody, UpdateShipmentBody, ShipmentStats
from .products import Product, CreateProductBody, UpdateProductBody, ProductStats
from .team import TeamMember, CreateTeamMemberBody, UpdateTeamMemberBody, TeamStats
from .users import User, CreateUserBody, UpdateUserBody, UserStats
from .analytics import PageView, AnalyticsStats, TrafficStats
from .media import Media, CreateMediaBody, UpdateMediaBody, MediaStats
from .user_groups import UserGroup, CreateUserGroupBody, UpdateUserGroupBody, UserGroupStats

__all__ = [
    "ApiResponse",
    "ListParams",
    "PaginatedMeta",
    "PaginatedResponse",
    "BlogAuthor",
    "BlogCategory",
    "BlogPost",
    "CreateBlogPostBody",
    "UpdateBlogPostBody",
    "CreateBlogCategoryBody",
    "UpdateBlogCategoryBody",
    "BlogAuthorResponse",
    "BlogStats",
    "EventCategory",
    "Event",
    "CreateEventBody",
    "UpdateEventBody",
    "CreateEventCategoryBody",
    "UpdateEventCategoryBody",
    "EventStats",
    "DonationCampaign",
    "Donation",
    "CreateDonationCampaignBody",
    "UpdateDonationCampaignBody",
    "DonationStats",
    "Order",
    "OrderItem",
    "CreateOrderBody",
    "UpdateOrderBody",
    "OrderStats",
    "Invoice",
    "InvoiceItem",
    "CreateInvoiceBody",
    "UpdateInvoiceBody",
    "InvoiceStats",
    "Transaction",
    "CreateTransactionBody",
    "UpdateTransactionBody",
    "TransactionStats",
    "Service",
    "CreateServiceBody",
    "UpdateServiceBody",
    "ServiceStats",
    "Appointment",
    "CreateAppointmentBody",
    "UpdateAppointmentBody",
    "AppointmentStats",
    "Vendor",
    "CreateVendorBody",
    "UpdateVendorBody",
    "VendorStats",
    "Banner",
    "CreateBannerBody",
    "UpdateBannerBody",
    "BannerStats",
    "Shipment",
    "CreateShipmentBody",
    "UpdateShipmentBody",
    "ShipmentStats",
    "Product",
    "CreateProductBody",
    "UpdateProductBody",
    "ProductStats",
    "TeamMember",
    "CreateTeamMemberBody",
    "UpdateTeamMemberBody",
    "TeamStats",
    "User",
    "CreateUserBody",
    "UpdateUserBody",
    "UserStats",
    "PageView",
    "AnalyticsStats",
    "TrafficStats",
    "Media",
    "CreateMediaBody",
    "UpdateMediaBody",
    "MediaStats",
    "UserGroup",
    "CreateUserGroupBody",
    "UpdateUserGroupBody",
    "UserGroupStats",
]
