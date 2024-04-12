"""userdata table created

Revision ID: b7df2d31bb21
Revises: ab386aa24a03
Create Date: 2024-04-10 15:57:44.581256

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7df2d31bb21'
down_revision: Union[str, None] = 'ab386aa24a03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('otp_table',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('Email', sa.String(), nullable=False),
    sa.Column('HashPassword', sa.String(), nullable=False),
    sa.Column('LoginTime', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('OTP', sa.String(), nullable=True),
    sa.Column('OTP_TimeLimit', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('Email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('otp_table')
    # ### end Alembic commands ###