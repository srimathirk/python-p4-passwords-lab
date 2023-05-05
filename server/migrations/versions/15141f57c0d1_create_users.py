"""create users

Revision ID: 15141f57c0d1
Revises: b72730abf5ef
Create Date: 2022-11-15 15:52:33.517166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15141f57c0d1'
down_revision = 'b72730abf5ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('_password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###