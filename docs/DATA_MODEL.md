# Data model

Core tables: `users`, `organizations`, `events`, `venues`, `airports`, `event_dates`, `websites`, `event_websites`, `taxa`, `event_taxa`, `countries`, `taxon_origin_countries`, `route_risks`, `evidence_items`, `actors`, `event_actors`, `risk_scores`, `lead_packages`, `audit_logs`.

All major records include UUID-compatible string primary keys plus `created_at` and `updated_at`. Venue and airport records store latitude/longitude plus WKT geometry placeholders; production PostGIS deployments can convert these to `geography(Point, 4326)` with GeoAlchemy2 migrations.

Risk scores are deterministic and explainable. Weights are documented in `backend/app/services/risk_scoring.py` and returned in the API response.
