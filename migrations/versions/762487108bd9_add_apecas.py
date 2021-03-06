"""Add apecas

Revision ID: 762487108bd9
Revises: f9239e9687c0
Create Date: 2020-08-28 00:47:11.985278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '762487108bd9'
down_revision = 'f9239e9687c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sdvx_apeca',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('texture', sa.String(), nullable=True),
    sa.Column('illustrator', sa.String(), nullable=True),
    sa.Column('rarity', sa.Integer(), nullable=True),
    sa.Column('sort_no', sa.Integer(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sdvx_apeca')
    # ### end Alembic commands ###
