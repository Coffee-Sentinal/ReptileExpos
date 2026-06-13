import uuid
from datetime import datetime, date
from sqlalchemy import String, DateTime, Date, Float, ForeignKey, Integer, Text, JSON, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
def uid(): return str(uuid.uuid4())
class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
class Organization(Base, TimestampMixin):
    __tablename__="organizations"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); name:Mapped[str]=mapped_column(String)
class User(Base, TimestampMixin):
    __tablename__="users"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); email:Mapped[str]=mapped_column(String, unique=True); role:Mapped[str]=mapped_column(String); organization_id:Mapped[str|None]=mapped_column(ForeignKey("organizations.id"), nullable=True)
class Country(Base, TimestampMixin):
    __tablename__="countries"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); name:Mapped[str]=mapped_column(String, unique=True); iso2:Mapped[str]=mapped_column(String(2))
class Venue(Base, TimestampMixin):
    __tablename__="venues"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); name:Mapped[str]=mapped_column(String); city:Mapped[str]=mapped_column(String); country:Mapped[str]=mapped_column(String); latitude:Mapped[float]=mapped_column(Float); longitude:Mapped[float]=mapped_column(Float); geom_wkt:Mapped[str]=mapped_column(String, default="POINT(0 0)")
class Event(Base, TimestampMixin):
    __tablename__="events"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); name:Mapped[str]=mapped_column(String); slug:Mapped[str]=mapped_column(String, unique=True); venue_id:Mapped[str]=mapped_column(ForeignKey("venues.id")); description:Mapped[str]=mapped_column(Text); status:Mapped[str]=mapped_column(String, default="monitoring"); confidence:Mapped[str]=mapped_column(String, default="unknown"); venue=relationship("Venue"); dates=relationship("EventDate", cascade="all,delete"); websites=relationship("EventWebsite", cascade="all,delete"); taxa=relationship("EventTaxon", cascade="all,delete"); evidence=relationship("EvidenceItem", cascade="all,delete"); routes=relationship("RouteRisk", cascade="all,delete"); risk_score=relationship("RiskScore", uselist=False, cascade="all,delete")
class EventDate(Base, TimestampMixin):
    __tablename__="event_dates"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); event_id:Mapped[str]=mapped_column(ForeignKey("events.id")); start_date:Mapped[date]=mapped_column(Date); end_date:Mapped[date]=mapped_column(Date); label:Mapped[str]=mapped_column(String, default="next known event")
class Airport(Base, TimestampMixin):
    __tablename__="airports"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); iata:Mapped[str]=mapped_column(String(3), unique=True); name:Mapped[str]=mapped_column(String); city:Mapped[str]=mapped_column(String); country:Mapped[str]=mapped_column(String); latitude:Mapped[float]=mapped_column(Float); longitude:Mapped[float]=mapped_column(Float); geom_wkt:Mapped[str]=mapped_column(String, default="POINT(0 0)")
class Website(Base, TimestampMixin):
    __tablename__="websites"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); name:Mapped[str]=mapped_column(String); url:Mapped[str]=mapped_column(String); type:Mapped[str]=mapped_column(String); notes:Mapped[str]=mapped_column(Text); confidence:Mapped[str]=mapped_column(String); last_checked_date:Mapped[date|None]=mapped_column(Date, nullable=True)
class EventWebsite(Base, TimestampMixin):
    __tablename__="event_websites"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); event_id:Mapped[str]=mapped_column(ForeignKey("events.id")); website_id:Mapped[str]=mapped_column(ForeignKey("websites.id")); website=relationship("Website"); __table_args__=(UniqueConstraint("event_id","website_id"),)
class Taxon(Base, TimestampMixin):
    __tablename__="taxa"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); scientific_name:Mapped[str]=mapped_column(String, unique=True); common_name:Mapped[str]=mapped_column(String); taxon_group:Mapped[str]=mapped_column(String); cites_appendix:Mapped[str]=mapped_column(String); eu_annex:Mapped[str]=mapped_column(String); native_range_countries:Mapped[list]=mapped_column(JSON, default=list); origin_countries:Mapped[list]=mapped_column(JSON, default=list); transit_countries:Mapped[list]=mapped_column(JSON, default=list); id_notes:Mapped[str]=mapped_column(Text)
class EventTaxon(Base, TimestampMixin):
    __tablename__="event_taxa"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); event_id:Mapped[str]=mapped_column(ForeignKey("events.id")); taxon_id:Mapped[str]=mapped_column(ForeignKey("taxa.id")); reason_for_inclusion:Mapped[str]=mapped_column(Text); evidence_basis:Mapped[str]=mapped_column(String); confidence:Mapped[str]=mapped_column(String); taxon=relationship("Taxon")
class TaxonOriginCountry(Base, TimestampMixin):
    __tablename__="taxon_origin_countries"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); taxon_id:Mapped[str]=mapped_column(ForeignKey("taxa.id")); country_id:Mapped[str]=mapped_column(ForeignKey("countries.id")); basis:Mapped[str]=mapped_column(String); confidence:Mapped[str]=mapped_column(String)
class RouteRisk(Base, TimestampMixin):
    __tablename__="route_risks"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); event_id:Mapped[str]=mapped_column(ForeignKey("events.id")); direction:Mapped[str]=mapped_column(String); origin:Mapped[str]=mapped_column(String); destination:Mapped[str]=mapped_column(String); transit_hubs:Mapped[list]=mapped_column(JSON, default=list); window_start:Mapped[date]=mapped_column(Date); window_end:Mapped[date]=mapped_column(Date); rationale:Mapped[str]=mapped_column(Text); confidence:Mapped[str]=mapped_column(String)
class EvidenceItem(Base, TimestampMixin):
    __tablename__="evidence_items"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); title:Mapped[str]=mapped_column(String); evidence_type:Mapped[str]=mapped_column(String); url:Mapped[str]=mapped_column(String); date_observed:Mapped[date]=mapped_column(Date); date_posted:Mapped[date|None]=mapped_column(Date, nullable=True); event_id:Mapped[str|None]=mapped_column(ForeignKey("events.id"), nullable=True); related_taxa:Mapped[list]=mapped_column(JSON, default=list); related_actor:Mapped[str|None]=mapped_column(String, nullable=True); summary:Mapped[str]=mapped_column(Text); extracted_red_flags:Mapped[list]=mapped_column(JSON, default=list); screenshot_path:Mapped[str|None]=mapped_column(String, nullable=True); content_hash:Mapped[str|None]=mapped_column(String, nullable=True); analyst_notes:Mapped[str]=mapped_column(Text); confidence:Mapped[str]=mapped_column(String)
class Actor(Base, TimestampMixin):
    __tablename__="actors"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); name:Mapped[str]=mapped_column(String); actor_type:Mapped[str]=mapped_column(String); notes:Mapped[str]=mapped_column(Text)
class EventActor(Base, TimestampMixin):
    __tablename__="event_actors"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); event_id:Mapped[str]=mapped_column(ForeignKey("events.id")); actor_id:Mapped[str]=mapped_column(ForeignKey("actors.id")); relationship_type:Mapped[str]=mapped_column(String)
class RiskScore(Base, TimestampMixin):
    __tablename__="risk_scores"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); event_id:Mapped[str]=mapped_column(ForeignKey("events.id"), unique=True); species_risk:Mapped[int]=mapped_column(Integer); online_signal_risk:Mapped[int]=mapped_column(Integer); route_risk:Mapped[int]=mapped_column(Integer); paperwork_risk:Mapped[int]=mapped_column(Integer); courier_export_risk:Mapped[int]=mapped_column(Integer); overall_score:Mapped[int]=mapped_column(Integer); priority:Mapped[str]=mapped_column(String); confidence:Mapped[str]=mapped_column(String); explanation:Mapped[dict]=mapped_column(JSON, default=dict)
class LeadPackage(Base, TimestampMixin):
    __tablename__="lead_packages"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); event_id:Mapped[str]=mapped_column(ForeignKey("events.id")); title:Mapped[str]=mapped_column(String); html:Mapped[str]=mapped_column(Text); caveat:Mapped[str]=mapped_column(Text)
class AuditLog(Base, TimestampMixin):
    __tablename__="audit_logs"; id:Mapped[str]=mapped_column(String, primary_key=True, default=uid); actor:Mapped[str]=mapped_column(String); action:Mapped[str]=mapped_column(String); entity_type:Mapped[str]=mapped_column(String); entity_id:Mapped[str]=mapped_column(String); details:Mapped[dict]=mapped_column(JSON, default=dict)
