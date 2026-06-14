# Data model

TypeScript interfaces live in `lib/types.ts`.

## JSON files
- `events.json`: event `id`, `name`, `venue`, `officialUrl`, `eventDates`, `knownFrequency`, `monitoringPriority`, `confidence`, `description`, placeholder flag, and source type.
- `taxa.json`: scientific/common name, taxon group, CITES appendix, EU annex, native range, possible origin countries, transit countries, reason, evidence basis, confidence, and identification notes.
- `event_taxa.json`: joins events to taxa with reason, evidence basis, and confidence.
- `websites.json`: public-safe website/platform category, URL, notes, confidence, last checked date, and public-safe flag.
- `event_websites.json`: joins events to websites.
- `evidence.json`: evidence type, optional URL, observation/post dates, related event/taxa, summary, red flags, analyst notes, confidence, and public-safe status.
- `airports.json`: IATA, name, city/country, coordinates, and linked event IDs.
- `route_risks.json`: inbound/outbound route-risk intersections, origin/transit/destination, relevant taxa, timing windows, rationale, confidence, and caveat.
- `countries.json`: country IDs and names.
- `lead_package_templates.json`: public-safe lead package templates.

Allowed confidence: `unknown`, `low`, `medium`, `high`. Allowed risk: `low`, `medium`, `high`, `critical`.
