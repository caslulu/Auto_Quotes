"""merge migrations

Revision ID: 97f19e0f6733
Revises: 6353e0415da8, add_placa_to_vehicles_json
Create Date: 2025-05-30 13:50:26.240877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97f19e0f6733'
down_revision = ('6353e0415da8', 'add_placa_to_vehicles_json')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
