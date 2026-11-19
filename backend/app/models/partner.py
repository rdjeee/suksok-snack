"""Partner model — specs/05-data-model.md §4.10 (BARU v1.2.0 — Epic E8: Mitra Kerjasama).

1:1 relationship dengan customers (customer_type='partner').
Mitra Kerjasama = institusi/organisasi (Ritel, Alfamart, Kantin Sekolah, dll).
"""
from sqlalchemy import TIMESTAMP, Column, Date, Enum, ForeignKey, Index, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base

# ENUM values
ORGANIZATION_TYPES = (
    "retail",
    "modern_retail",
    "school_cafeteria",
    "campus_organization",
    "cooperative",
    "event_organizer",
    "other",
)
PARTNERSHIP_TYPES = ("ongoing", "one_time")
AGREEMENT_STATUSES = ("pending", "active", "completed", "inactive", "rejected")


class Partner(Base):
    """Mitra Kerjasama — institusi/organisasi yang bekerja sama dengan Suksok Snack.

    1:1 dengan Customer (customer_type='partner').
    - ongoing: berkelanjutan (Alfamart, Kantin Sekolah) → checkout kapan saja
    - one_time: sekali event (Expo, Bazar) → checkout hanya saat ada sponsor_event aktif
    """

    __tablename__ = "partners"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id", ondelete="CASCADE"), nullable=False, unique=True)
    organization_name = Column(String(150), nullable=False)
    organization_type = Column(
        Enum(*ORGANIZATION_TYPES, name="organization_type_enum"),
        nullable=False,
    )
    partnership_type = Column(
        Enum(*PARTNERSHIP_TYPES, name="partnership_type_enum"),
        nullable=False,
        default="ongoing",
    )
    agreement_status = Column(
        Enum(*AGREEMENT_STATUSES, name="agreement_status_enum"),
        default="pending",
    )
    agreement_start_date = Column(Date, nullable=True)
    agreement_end_date = Column(Date, nullable=True)  # NULL for ongoing
    contact_person = Column(String(100), nullable=True)
    contact_phone = Column(String(20), nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    # Relationship to sponsor_events (1 partner → many events for re-apply)
    sponsor_events = relationship("SponsorEvent", back_populates="partner", cascade="all, delete-orphan")

    __table_args__ = (
        Index("idx_partner_type", "partnership_type"),
        Index("idx_partner_status", "agreement_status"),
    )

    def __repr__(self) -> str:
        return (
            f"<Partner id={self.id} org={self.organization_name!r} "
            f"type={self.partnership_type!r} status={self.agreement_status!r}>"
        )
