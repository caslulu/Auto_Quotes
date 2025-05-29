"""merge heads

Revision ID: 6353e0415da8
Revises: add_spouse_fields, add_vehicles_json_to_cotacao
Create Date: 2025-05-28 23:52:49.588907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6353e0415da8'
down_revision = ('add_spouse_fields', 'add_vehicles_json_to_cotacao')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
