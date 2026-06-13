# Architecture

ExpoWatch is a monorepo with `backend/` and `frontend/` services orchestrated by Docker Compose.

- FastAPI exposes REST endpoints under `/api`.
- SQLAlchemy models define normalized event, venue, airport, taxa, website, evidence, route-risk, risk-score, lead-package, user, organization, actor, and audit-log tables.
- Alembic owns schema creation.
- Next.js server components fetch API data and render operational pages; Leaflet is dynamically loaded client-side.
- Sensitive route-risk logic remains server-side. UI labels all route data as route-risk intersections and recommended verification points.

External adapter foundations:
- `FlightScheduleProvider`, `MockFlightScheduleProvider`, `OAGProvider`, `CiriumProvider`, `FlightAwareProvider`.
- `SpeciesPlusService` falls back to seed data when no token is configured.
