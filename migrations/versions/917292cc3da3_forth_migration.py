"""forth Migration

Revision ID: 917292cc3da3
Revises: f328fb634b20
Create Date: 2019-07-10 23:45:49.131717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '917292cc3da3'
down_revision = 'f328fb634b20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('subscription', 'email',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.create_unique_constraint(None, 'subscription', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subscription', type_='unique')
    op.alter_column('subscription', 'email',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###
