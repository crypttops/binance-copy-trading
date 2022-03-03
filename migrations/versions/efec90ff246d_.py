"""empty message

Revision ID: efec90ff246d
Revises: e0eba30e8a6e
Create Date: 2022-03-03 13:16:31.979769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efec90ff246d'
down_revision = 'e0eba30e8a6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('botconfigs', sa.Column('leverage', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('botconfigs', 'leverage')
    # ### end Alembic commands ###
