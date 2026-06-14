# Data sources

This static MVP ships with public-safe seed/demo data. Optional refresh scripts must not require secrets or private scraping.

- **OurAirports**: open airport coordinates via CSV. Used for possible airport enrichment.
- **GDELT**: public news/event monitoring. Results require analyst review before any public evidence entry is updated.
- **Species+**: possible future CITES/taxonomic enrichment. The static script falls back to local seed data when no token is present.
- **CITES Trade Database**: possible future trade-record review by analysts; not automated in this MVP.
- **GBIF**: possible future distribution/taxonomy support; not automated in this MVP.
- **OpenFlights**: historical route data only. It is not current flight schedules and must not be presented as live flight intelligence.
- **Manual analyst-curated sources**: public official event pages, journalism, seizure reports, and public-safe summaries. Do not include private scraped content.
