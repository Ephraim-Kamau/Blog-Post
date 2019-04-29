"""Initial Migration

Revision ID: d5e30059279f
Revises: 75c7c2cff20e
Create Date: 2019-04-29 15:30:26.317313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5e30059279f'
down_revision = '75c7c2cff20e'
branch_labels = None
depends_on = None

# Add email and UserMixin to class User"
def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###