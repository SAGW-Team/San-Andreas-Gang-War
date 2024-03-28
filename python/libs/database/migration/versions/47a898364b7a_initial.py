"""'initial'

Revision ID: 47a898364b7a
Revises: 8f591c7ee369
Create Date: 2024-03-28 21:13:18.557455

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '47a898364b7a'
down_revision: Union[str, None] = '8f591c7ee369'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('PlayerSettings', sa.Column('outdated_version_warning', sa.Boolean(), nullable=True, server_default=sa.false()))
    op.add_column('PlayerSettings', sa.Column('use_squad_tag_in_text', sa.Boolean(), nullable=True, server_default=sa.false()))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Vehicle', 'uid',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('SquadRankPermissions', 'uid',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('SquadRank', 'uid',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('SquadMember', 'uid',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('SquadGangZones', 'uid',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('Squad', 'uid',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('ServerAnalytics', 'uid',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('PlayerSettings', 'uid',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.drop_column('PlayerSettings', 'use_squad_tag_in_text')
    op.drop_column('PlayerSettings', 'outdated_version_warning')
    op.alter_column('PlayerFreeroamGunSlots', 'uid',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('Player', 'pin',
               existing_type=sa.String(length=6),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.alter_column('Player', 'uid',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('House', 'uid',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('GangZone', 'uid',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('AdminSavedPositions', 'uid',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('AdminLog', 'uid',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###