"""Sakha CMS modules package."""

from .blog import BlogModule
from .events import EventsModule
from .donations import DonationsModule
from .orders import OrdersModule
from .invoices import InvoicesModule
from .transactions import TransactionsModule
from .services import ServicesModule
from .appointments import AppointmentsModule
from .vendors import VendorsModule
from .banners import BannersModule
from .shipments import ShipmentsModule
from .products import ProductsModule
from .team import TeamModule
from .users import UsersModule
from .media import MediaModule
from .analytics import AnalyticsModule
from .user_groups import UserGroupsModule

__all__ = [
    "BlogModule",
    "EventsModule",
    "DonationsModule",
    "OrdersModule",
    "InvoicesModule",
    "TransactionsModule",
    "ServicesModule",
    "AppointmentsModule",
    "VendorsModule",
    "BannersModule",
    "ShipmentsModule",
    "ProductsModule",
    "TeamModule",
    "UsersModule",
    "MediaModule",
    "AnalyticsModule",
    "UserGroupsModule",
]
