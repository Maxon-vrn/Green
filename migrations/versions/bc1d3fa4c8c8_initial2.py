"""Initial2

Revision ID: bc1d3fa4c8c8
Revises: 7df5a5cc63df
Create Date: 2024-07-22 13:39:02.952828

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc1d3fa4c8c8'
down_revision: Union[str, None] = '7df5a5cc63df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_id', table_name='user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_user_id', 'user', ['id'], unique=True)
    # ### end Alembic commands ###
