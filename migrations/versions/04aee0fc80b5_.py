"""empty message

Revision ID: 04aee0fc80b5
Revises: 81b2b0256528
Create Date: 2017-08-02 00:31:01.940537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04aee0fc80b5'
down_revision = '81b2b0256528'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hot_search',
    sa.Column('id_', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id_')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hot_search')
    # ### end Alembic commands ###
