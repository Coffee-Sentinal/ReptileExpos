"""initial schema
Revision ID: 0001_initial
Revises:
Create Date: 2026-06-13
"""
from alembic import op
import sqlalchemy as sa
revision='0001_initial'; down_revision=None; branch_labels=None; depends_on=None
def upgrade():
    from app.core.database import Base
    from app.models import models
    bind = op.get_bind()
    Base.metadata.create_all(bind)
def downgrade():
    from app.core.database import Base
    Base.metadata.drop_all(op.get_bind())
