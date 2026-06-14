from enum import StrEnum
from fastapi import Header
from app.core.config import settings
class Role(StrEnum):
    admin="admin"; analyst="analyst"; viewer="viewer"; agency_partner="agency_partner"
def current_role(x_mock_role: str | None = Header(default=None)) -> Role:
    return Role(x_mock_role or settings.mock_auth_role)
