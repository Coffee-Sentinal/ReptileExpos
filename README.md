# ExpoWatch

ExpoWatch is a zero-cost, static GitHub Pages-compatible MVP for lawful OSINT and analytical planning around reptile/exotics expo monitoring priorities. It uses public/open-source and mock seed data only.

## What the static MVP does
- Maps international reptile/exotics expo demo events.
- Tracks event dates and monitoring windows.
- Links public-safe websites/platform categories.
- Shows proxy taxa, evidence examples, route-risk intersections, and lead package previews.
- Calculates deterministic explainable monitoring-priority scores in the browser/static build.

## What it does not do
- No backend, database, Docker, server runtime, paid API, authentication provider, or API keys.
- No private scraping, login bypassing, account automation, live flight schedules, or sensitive operational intelligence.
- No claim that any event, route, seller, courier, airline, vendor, or flight is criminal.

## Safety disclaimer
Static demo using public/open-source and mock data. Intelligence support only. Not proof of criminality. Use cautious language: risk indicator, monitoring priority, route-risk intersection, possible origin country, recommended verification, and confidence level.

## Local installation
```bash
npm install
```

## Local development
```bash
npm run dev
```
Open <http://localhost:3000>.

## Static build
```bash
npm run build
```
Next.js is configured with `output: "export"`; the static site is written to `out/`.

## Branch-based GitHub Pages deployment from `/docs`
This repository is configured so you can deploy from the `main` branch without GitHub Actions.

1. Build the GitHub Pages export into `/docs`:
   ```bash
   npm run build:pages
   ```
2. Commit the updated `/docs` folder:
   ```bash
   git add docs
   git commit -m "Build GitHub Pages static site"
   git push origin main
   ```
3. In GitHub, open **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select branch: `main`.
6. Select folder: `/docs`.
7. Save.

The `build:pages` script sets the GitHub Pages base path to `/${REPOSITORY_NAME}` by default, runs the static Next.js export, copies `out/` into `/docs`, and writes `docs/.nojekyll`. To override the base path, run:

```bash
NEXT_PUBLIC_BASE_PATH=/your-repo-name npm run build:pages
```

The committed `docs/index.html` is a safe placeholder until you run `npm run build:pages`; after the script runs, `/docs` contains the final exported website files.

## Linting and validation
```bash
npm run lint
python scripts/validate_data.py
```

## Documentation
Project documentation lives in `project-docs/` so the `/docs` folder can be reserved for GitHub Pages static output.

## Editing seed data
Edit readable JSON files in `public/data/`. Keep stable IDs and public-safe content only. Do not include private suspect data, phone numbers, sensitive intelligence, or scraped private platform data.

## Add a new event
1. Add the event to `public/data/events.json` with `id`, `venue`, coordinates, date, confidence, and monitoring priority.
2. Link taxa in `public/data/event_taxa.json`.
3. Add websites in `public/data/websites.json` and `public/data/event_websites.json`.
4. Add public-safe evidence in `public/data/evidence.json`.
5. Add nearby airports and route-risk intersections if appropriate.
6. Run `python scripts/validate_data.py`.

## Add proxy taxa
Add the taxon to `public/data/taxa.json`, then reference its stable ID from `event_taxa.json` and `route_risks.json` as needed.

## Add evidence
Add a public-safe entry to `public/data/evidence.json`. Use summaries and red flags; do not upload files or private screenshots in this prototype.

## Regenerate route-risk data
```bash
python scripts/build_route_risk.py
```
The current MVP validates static corridors. Optional future scripts can derive corridors from open data.

## Open-data refresh
`.github/workflows/update-open-data.yml` can run manually or weekly. It attempts optional public data fetches, validates data, and commits changed public data files if any.

## Known limitations
- Static filters are UI scaffolding; advanced client-side filtering can be added next.
- Route-risk corridors are static/demo and not current schedules.
- Lead package export uses browser print/save-as-PDF only.
- No authentication; this is a public-safe prototype.

## Roadmap
See `project-docs/ROADMAP.md`.
