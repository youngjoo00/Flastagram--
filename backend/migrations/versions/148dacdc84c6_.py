"""empty message

Revision ID: 148dacdc84c6
Revises: aabc927677a4
Create Date: 2022-12-12 15:40:11.083561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '148dacdc84c6'
down_revision = 'aabc927677a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_liker',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['Post.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_liker')
    # ### end Alembic commands ###