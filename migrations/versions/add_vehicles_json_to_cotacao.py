"""add vehicles_json to cotacao

Revision ID: add_vehicles_json_to_cotacao
Revises: 
Create Date: 2025-05-28
"""
from alembic import op
import sqlalchemy as sa

revision = 'add_vehicles_json_to_cotacao'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('cotacao') as batch_op:
        batch_op.add_column(sa.Column('vehicles_json', sa.Text(), nullable=False, server_default='[]'))
        batch_op.drop_column('financiado')
        batch_op.drop_column('vin')
        batch_op.drop_column('tempo_com_veiculo')

def downgrade():
    with op.batch_alter_table('cotacao') as batch_op:
        batch_op.add_column(sa.Column('financiado', sa.String(50), nullable=False, server_default=''))
        batch_op.add_column(sa.Column('vin', sa.String(50), nullable=False, server_default=''))
        batch_op.add_column(sa.Column('tempo_com_veiculo', sa.String(50), nullable=False, server_default=''))
        batch_op.drop_column('vehicles_json')
