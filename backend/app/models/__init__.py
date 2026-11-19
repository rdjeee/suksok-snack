"""SQLAlchemy models for Suksok Snack.

Importing this package imports all model classes so that:
  1. Alembic autogenerate can detect them.
  2. `Base.metadata.create_all()` creates every table.

Spec reference: specs/05-data-model.md (11 tables, ERD, SQL DDL).
"""
from app.models.admin import Admin
from app.models.customer import Customer
from app.models.notification import Notification
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.partner import Partner
from app.models.payment import Payment
from app.models.product import Product
from app.models.product_variant import ProductVariant
from app.models.setting import Setting
from app.models.sponsor_event import SponsorEvent

__all__ = [
    "Admin",
    "Customer",
    "Partner",
    "SponsorEvent",
    "Product",
    "ProductVariant",
    "Order",
    "OrderItem",
    "Payment",
    "Notification",
    "Setting",
]
