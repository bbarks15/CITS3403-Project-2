"""temp

Revision ID: 9d8a56de5813
Revises: 42f97aaf0d92
Create Date: 2020-05-25 12:03:16.982903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d8a56de5813'
down_revision = '42f97aaf0d92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('temp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('temp')
    # ### end Alembic commands ###
