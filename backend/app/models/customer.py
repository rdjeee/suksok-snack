"""Customer model — specs/05-data-model.md §4.2.

NOTIF-007 (v1.0.7): Added acquisition_channel field.
NOTIF-009 (v1.2.0): BREAKING — customer_type enum renamed:
  retail → partner (Mitra Kerjasama)
  public → consumer (Konsumen Akhir)
"""
from sqlalchemy import BOOLEAN, TIMESTAMP, Column, Enum, Index, Integer, String, Text
from sqlalchemy.sql import func

from app.core.database import Base

# ENUM values — DB-agnostic: MySQL native ENUM, SQLite VARCHAR + CHECK.
# NOTIF-009: renamed from ('retail', 'public') to ('partner', 'consumer')
CUSTOMER_TYPES = ("partner", "consumer")

# NOTIF-007: acquisition channel values
ACQUISITION_CHANNELS = ("direct", "reseller", "social_media", "word_of_mouth", "other")


class Customer(Base):
    """Customer account — Mitra Kerjasama (partner) or Konsumen Akhir (consumer)."""

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)  # bcrypt, 12 rounds
    name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    address = Column(Text, nullable=False)
    customer_type = Column(
        Enum(*CUSTOMER_TYPES, name="customer_type_enum"),
        nullable=False,
        default="consumer",  # NOTIF-009: default changed from 'public' to 'consumer'
    )
    # NOTIF-007: Track darimana customer berasal (Masalah 6 — pemasaran belum tergabungkan)
    acquisition_channel = Column(String(50), default="direct")
    fcm_token = Column(Text, nullable=True)  # Firebase Cloud Messaging token (PWA push)
    is_active = Column(BOOLEAN, default=True)  # soft delete flag
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        Index("idx_customer_type", "customer_type"),
        Index("idx_acquisition_channel", "acquisition_channel"),  # NOTIF-007
    )

    def __repr__(self) -> str:
        return f"<Customer id={self.id} email={self.email!r} type={self.customer_type!r}>"
