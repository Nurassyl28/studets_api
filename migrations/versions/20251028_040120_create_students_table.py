
"""create students table

Revision ID: 20251028_040120
Revises: 
Create Date: 2025-10-28T04:01:20

"""

from alembic import op
import sqlalchemy as sa


revision = '20251028_040120'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'students',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('age', sa.Integer(), nullable=False),
        sa.Column('group', sa.String(length=64), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('avatar_url', sa.String(length=1024), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('NOW()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('NOW()'), nullable=False),
    )
    op.create_unique_constraint('uq_students_email', 'students', ['email'])
    op.create_index('ix_students_id', 'students', ['id'], unique=False)

def downgrade() -> None:
    op.drop_index('ix_students_id', table_name='students')
    op.drop_constraint('uq_students_email', 'students', type_='unique')
    op.drop_table('students')
