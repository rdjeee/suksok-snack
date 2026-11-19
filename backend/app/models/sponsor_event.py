"""SponsorEvent model — specs/05-data-model.md §4.11 (BARU v1.2.0 — Epic E8: Mitra Kerjasama).

1:N relationship dengan partners (1 partner bisa multiple events untuk re-apply).
Track event/kegiatan untuk one_time partnership (Expo, Bazar, Sponsor).
"""
from sqlalchemy import TIMESTAMP, Column, Date, Enum, ForeignKey, Index, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base

# ENUM values
EVENT_TYPES = ("expo", "bazar", "sponsor", "collaboration")
EVENT_STATUSES = ("planned", "ongoing", "completed", "cancelled")


class SponsorEvent(Base):
    """Sponsor/event record untuk partner (terutama one_time partnership).

    - planned: sudah dibuat, belum mulai
    - ongoing: sedang berlangsung (start_date ≤ today ≤ end_date)
    - completed: sudah selesai (today > end_date) → trigger auto-expire partner
    - cancelled: dibatalkan
    """

    __tablename__ = "sponsor_events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    partner_id = Column(Integer, ForeignKey("partners.id", ondelete="CASCADE"), nullable=False)
    event_name = Column(String(200), nullable=False)
    event_type = Column(
        Enum(*EVENT_TYPES, name="event_type_enum"),
        default="expo",
    )
    event_start_date = Column(Date, nullable=False)
    event_end_date = Column(Date, nullable=False)
    event_location = Column(String(200), nullable=True)
    description = Column(Text, nullable=True)
    status = Column(
        Enum(*EVENT_STATUSES, name="event_status_enum"),
        default="planned",
    )
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    # Relationship back to partner
    partner = relationship("Partner", back_populates="sponsor_events")

    __table_args__ = (
        Index("idx_event_status", "status"),
        Index("idx_event_dates", "event_start_date", "event_end_date"),
    )

    def __repr__(self) -> str:
        return (
            f"<SponsorEvent id={self.id} name={self.event_name!r} "
            f"type={self.event_type!r} status={self.status!r}>"
        )
