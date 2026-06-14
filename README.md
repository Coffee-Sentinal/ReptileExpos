# ExpoWatch

ExpoWatch is a simple static HTML/CSS/JavaScript dashboard for event-risk intelligence organization around reptile and exotics expo monitoring priorities. It maps expo locations, event dates, linked public websites, high-risk proxy taxa, possible origin countries, route-risk corridors, evidence examples, and printable lead packages.

## What this app is
- A single-page GitHub Pages dashboard using `index.html`, `style.css`, `app.js`, and `data/*.json`.
- An analytical dashboard for event monitoring and recommended verification planning.
- A no-install app that uses free CDN libraries: Leaflet for maps and PapaParse for optional OurAirports CSV parsing.

## What this app is not
- Not a backend application.
- Not a database.
- Not a live flight tracker.
- Not an authentication system.
- Not a scraper of private groups or protected platforms.
- Not a case-management or enforcement records system.

## Safety language
Use concise operational labels: risk indicator, monitoring priority, possible origin country, route-risk corridor, recommended verification, and confidence level.

## Launch locally
Open `index.html` in a browser. The app includes bundled fallback data in `app.js` so it can still render if the browser blocks `file://` JSON fetches. On GitHub Pages, it loads `data/*.json` normally.

## Launch on GitHub Pages from the repository root
1. Push these files to the `main` branch.
2. Go to repository **Settings**.
3. Go to **Pages**.
4. Select **Deploy from branch**.
5. Select branch: `main`.
6. Select folder: `/ (root)`.
7. Save.
8. Wait for GitHub Pages to finish publishing, then open `https://<your-user-or-org>.github.io/<repo-name>/`.

No build step, npm install, GitHub Actions deployment workflow, server, API key, or database is required. The root `index.html` is the app entry point, and `.nojekyll` is included so GitHub Pages serves the static files as-is.

### If GitHub Pages shows this README instead of the dashboard
That means Pages is not serving the committed root `index.html`. Check these items:

1. Confirm the latest commit on `main` contains `index.html`, `style.css`, `app.js`, and `data/*.json` at the repository root.
2. In **Settings → Pages**, confirm branch is `main` and folder is `/ (root)`, not `/docs`.
3. Wait a few minutes and hard-refresh the Pages URL. GitHub Pages can cache an older build briefly.
4. Open the URL ending in `/index.html` directly. If that works, the root URL cache is stale.
5. If it still shows README content, push a fresh commit after verifying `index.html` exists in the GitHub web UI.


## Current root-file sanity check

For GitHub Pages from `main` + `/ (root)`, these files must appear at the repository root in GitHub's web UI before Pages is refreshed:

- `index.html`
- `style.css`
- `app.js`
- `.nojekyll`
- `data/events.json`

If the Pages URL renders this README instead of the dashboard, GitHub Pages is serving an older commit or the wrong folder. Confirm the settings and open `/index.html` directly after the latest commit is on `main`.

## Data files
- `data/events.json` — expo/event profiles, dates, priorities, linked websites, taxa, evidence, origins, and consumers.
- `data/taxa.json` — proxy taxa library with CITES/EU status, origin countries, evidence basis, and officer-facing notes.
- `data/websites.json` — websites and online source categories.
- `data/evidence.json` — evidence/news examples.
- `data/airports.json` — local airport coordinates.
- `data/routes.json` — static route-risk corridors marked as not live flight intelligence.
- `data/countries.json` — country list.

## How to edit data files
Edit the JSON files in `data/` with stable IDs. Keep content appropriate for partner review. Do not add private suspect data, private screenshots, phone numbers, account information, or sensitive operational intelligence.

## How to add an event
1. Add a new object to `data/events.json`.
2. Add or reuse website IDs in `linked_website_ids`.
3. Add or reuse taxon IDs in `proxy_taxa_ids`.
4. Add evidence IDs in `evidence_ids`.
5. Add route-risk corridor objects to `data/routes.json` if appropriate.

## How to add taxa
Add a new object to `data/taxa.json`, then reference its `id` from event `proxy_taxa_ids` and route `relevant_taxa_ids`.

## How to use GDELT search
Open the “Evidence & News Monitor” tab, enter a keyword and optional event/species/date filters, then click “Search public news.” If the browser blocks the query, use the displayed GDELT query URL manually.

## How to use GBIF lookup
Open the “High-Risk Taxa” tab and click “Check GBIF taxonomy/range” on a taxon card. GBIF results provide biological context and taxonomy/range references.

## Data editor / import-export
The editor tab lets you add an evidence draft in browser memory, save edits to `localStorage`, export edited JSON, import JSON, or reset to bundled demo data. It does not write back to GitHub.

## Limitations
- Seed data is demo/open-source placeholder data.
- Route-risk corridors are plausible analytical corridors, not live flights or current schedules.
- GDELT, GBIF, and OurAirports requests depend on browser/network/CORS availability.
- Browser local edits remain local unless exported and manually committed.

## Caveat
ExpoWatch is an event-risk and route-risk dashboard for partner review and monitoring prioritization.
