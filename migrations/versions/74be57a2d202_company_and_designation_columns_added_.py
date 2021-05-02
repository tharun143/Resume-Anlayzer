"""company and designation columns added in users

Revision ID: 74be57a2d202
Revises: 969549761719
Create Date: 2020-05-12 01:13:58.137609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74be57a2d202'
down_revision = '969549761719'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('company', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('designation', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'designation')
    op.drop_column('user', 'company')
    # ### end Alembic commands ###
