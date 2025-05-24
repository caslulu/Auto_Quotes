"""add spouse fields to cotacao

Revision ID: add_spouse_fields
Revises: ad8d82eb3cbe
Create Date: 2025-05-23

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'add_spouse_fields'
down_revision = 'ad8d82eb3cbe'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('cotacao', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nome_conjuge', sa.String(length=100)))
        batch_op.add_column(sa.Column('data_nascimento_conjuge', sa.String(length=50)))
        batch_op.add_column(sa.Column('documento_conjuge', sa.String(length=50)))

def downgrade():
    with op.batch_alter_table('cotacao', schema=None) as batch_op:
        batch_op.drop_column('nome_conjuge')
        batch_op.drop_column('data_nascimento_conjuge')
        batch_op.drop_column('documento_conjuge')
