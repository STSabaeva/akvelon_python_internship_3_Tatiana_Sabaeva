"""'added'

Revision ID: 98bf4782a28f
Revises: 
Create Date: 2021-05-14 21:48:17.452117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98bf4782a28f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=False),
    sa.Column('last_name', sa.String(length=150), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email')
    )
    op.create_table('finance',
    sa.Column('trans_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('sum_of_trans', sa.Float(precision=150), nullable=False),
    sa.Column('trans_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('trans_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('finance')
    op.drop_table('user')
    # ### end Alembic commands ###
