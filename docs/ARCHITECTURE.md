# Architecture

ExpoWatch is a static Next.js App Router site exported with `output: "export"` and deployable to GitHub Pages. It has no backend, no database, and no server runtime.

## Data flow
1. Analysts edit JSON/CSV seed data under `public/data` and `data/raw`.
2. Optional scripts in `scripts/` fetch or prepare public/open data and validate referential integrity.
3. Next.js imports JSON at build time through `lib/data.ts`.
4. Pages render static HTML/JS for dashboard, maps, event detail pages, calendar, taxa, evidence, routes, and lead packages.

## Deployment
`.github/workflows/deploy-pages.yml` installs Node, builds the static export, uploads `out/`, and deploys with GitHub Pages. `NEXT_PUBLIC_BASE_PATH` supports repository project pages.

## Future backend path
If operational needs require protected data, migrate sensitive features to a secure backend with authentication, RBAC, audit logs, encrypted storage, and partner-only route-risk controls. Keep this public static version limited to demo/open data.
