from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    database_url: str = "sqlite:///./expowatch.db"
    cors_origins: str = "http://localhost:3000"
    mock_auth_role: str = "analyst"
    speciesplus_token: str | None = None
settings = Settings()
