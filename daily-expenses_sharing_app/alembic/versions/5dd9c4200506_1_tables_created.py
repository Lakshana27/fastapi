"""1_tables_created

Revision ID: 5dd9c4200506
Revises: 20bd0073986e
Create Date: 2024-07-28 17:41:07.040534

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5dd9c4200506'
down_revision: Union[str, None] = '20bd0073986e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('splits', sa.Column('created_by', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('splits', 'created_by')
    # ### end Alembic commands ###
