# ExpoWatch

ExpoWatch is a secure internal MVP for lawful OSINT organization, event-based wildlife trade monitoring priorities, route-risk intersection review, proxy taxa tracking, and enforcement partner lead-package previews. It uses cautious intelligence language: indicators are not proof of criminality.

## Stack
- Frontend: Next.js App Router, TypeScript, Tailwind CSS, Leaflet/react-leaflet.
- Backend: FastAPI, Pydantic, SQLAlchemy 2.x, Alembic.
- Database: PostgreSQL/PostGIS via Docker Compose. The SQLAlchemy model keeps WKT coordinate fields for MVP portability and documents the PostGIS migration path.

## Local setup
```bash
cp .env.example .env
docker compose up --build
```
Frontend: http://localhost:3000. Backend API docs: http://localhost:8000/docs.

## Migrations and seeding
```bash
cd backend
alembic upgrade head
python -m app.seed.seed_data
```
Docker runs both automatically for the backend service.

## Development commands
```bash
cd backend && pytest
cd frontend && npm install && npm run build
```

## Safety and legal-use notes
- Internal use only; outputs are intelligence support, not proof of criminality.
- Do not scrape private platforms, bypass logins, defeat rate limits, or automate account interactions.
- Route-risk data is mock/seeded in the MVP and should be shared only with authorized partners.
- Use recommended verification language and avoid guilt-implying conclusions from single indicators.

## Current limitations
- Mock authentication and role header only.
- PDF export is stubbed as “MVP export pending”; HTML lead preview is implemented.
- Flight and SpeciesPlus adapters are placeholders that gracefully fall back to seed data.
- Manual evidence POST exists; file upload/hash automation is future work.

## Next steps
See `docs/ROADMAP.md`.
