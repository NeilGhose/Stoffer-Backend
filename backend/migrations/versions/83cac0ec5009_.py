"""empty message

Revision ID: 83cac0ec5009
Revises: 52aaee29aa13
Create Date: 2022-12-28 19:54:34.463257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83cac0ec5009'
down_revision = '52aaee29aa13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sm_auth',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sm_type', sa.String(length=20), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('refresh_key', sa.String(length=255), nullable=True),
    sa.Column('author_key', sa.String(length=255), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sm_auth')
    # ### end Alembic commands ###