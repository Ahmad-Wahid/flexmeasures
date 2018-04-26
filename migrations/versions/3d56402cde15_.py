"""empty message

Revision ID: 3d56402cde15
Revises: d3440de27ab9
Create Date: 2018-04-10 16:42:38.892648

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3d56402cde15'
down_revision = 'd3440de27ab9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bvp_users', 'current_login_at')
    op.drop_column('bvp_users', 'last_login_ip')
    op.drop_column('bvp_users', 'current_login_ip')
    op.drop_column('bvp_users', 'confirmed_at')


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bvp_users', sa.Column('current_login_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('bvp_users', sa.Column('last_login_ip', postgresql.VARCHAR(100), autoincrement=False, nullable=True))
    op.add_column('bvp_users', sa.Column('current_login_ip', postgresql.VARCHAR(100), autoincrement=False, nullable=True))
    op.add_column('bvp_users', sa.Column('confirmed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
