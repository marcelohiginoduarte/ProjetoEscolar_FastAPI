"""Adicionando campo 'username' ao modelo Usuario

Revision ID: 7740e597ab7b
Revises: c7796422cec1
Create Date: 2024-12-05 11:14:41.318373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7740e597ab7b'
down_revision: Union[str, None] = 'c7796422cec1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Usuarios', sa.Column('username', sa.Integer(), nullable=True))
    op.drop_index('ix_Usuarios_user', table_name='Usuarios')
    op.create_index(op.f('ix_Usuarios_username'), 'Usuarios', ['username'], unique=False)
    op.drop_column('Usuarios', 'user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Usuarios', sa.Column('user', sa.INTEGER(), nullable=True))
    op.drop_index(op.f('ix_Usuarios_username'), table_name='Usuarios')
    op.create_index('ix_Usuarios_user', 'Usuarios', ['user'], unique=False)
    op.drop_column('Usuarios', 'username')
    # ### end Alembic commands ###