from app.core.config import settings
class SpeciesPlusService:
    def lookup(self, scientific_name: str, fallback: dict | None = None) -> dict:
        if not settings.speciesplus_token:
            return {"source":"seed_fallback", **(fallback or {"scientific_name": scientific_name})}
        return {"source":"speciesplus_pending", **(fallback or {"scientific_name": scientific_name})}
