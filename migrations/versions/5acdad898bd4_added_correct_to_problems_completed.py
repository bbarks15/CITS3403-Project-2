"""added correct to problems completed

Revision ID: 5acdad898bd4
Revises: 1df7bc107f87
Create Date: 2020-05-24 19:35:16.371942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5acdad898bd4'
down_revision = '1df7bc107f87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_problems_completed_correct'), 'problems_completed', ['correct'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_problems_completed_correct'), table_name='problems_completed')
    # ### end Alembic commands ###
