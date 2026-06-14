# Architecture

ExpoWatch is a static Next.js App Router site exported with `output: "export"` and deployable to GitHub Pages. It has no backend, no database, and no server runtime.

## Data flow
1. Analysts edit JSON/CSV seed data under `public/data` and `data/raw`.
2. Optional scripts in `scripts/` fetch or prepare public/open data and validate referential integrity.
3. Next.js imports JSON at build time through `lib/data.ts`.
4. Pages render static HTML/JS for dashboard, maps, event detail pages, calendar, taxa, evidence, routes, and lead packages.

## Deployment
For branch-based GitHub Pages, run `npm run build:pages`; the script sets `NEXT_PUBLIC_BASE_PATH`, builds the static export, copies `out/` into `/docs`, and writes `docs/.nojekyll`. Configure GitHub Pages to deploy from `main` and `/docs`.

## Future backend path
If operational needs require protected data, migrate sensitive features to a secure backend with authentication, RBAC, audit logs, encrypted storage, and partner-only route-risk controls. Keep this public static version limited to demo/open data.
