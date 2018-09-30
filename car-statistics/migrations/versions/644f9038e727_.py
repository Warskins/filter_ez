"""empty message

Revision ID: 644f9038e727
Revises: 
Create Date: 2018-09-23 12:39:13.281932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '644f9038e727'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('path', sa.String(), nullable=False),
    sa.Column('attributes', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('filter',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('params', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('confirmed_date', sa.DateTime(), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('dataset',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('included_rows', sa.ARRAY(sa.Integer()), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('filter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['filter_id'], ['filter.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dataset')
    op.drop_table('users')
    op.drop_table('filter')
    op.drop_table('file')
    # ### end Alembic commands ###
