"""add placa to vehicles_json in cotacao

Revision ID: add_placa_to_vehicles_json
Revises: add_vehicles_json_to_cotacao
Create Date: 2025-05-29
"""
from alembic import op
import sqlalchemy as sa

revision = 'add_placa_to_vehicles_json'
down_revision = 'add_vehicles_json_to_cotacao'
branch_labels = None
depends_on = None

def upgrade():
    # Como vehicles_json é um campo JSON/texto, não é necessário alterar o schema,
    # mas esta migration serve para controle de versão.
    pass

def downgrade():
    pass
