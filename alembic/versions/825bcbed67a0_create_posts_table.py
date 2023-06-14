"""create posts table

Revision ID: 825bcbed67a0
Revises: 
Create Date: 2023-06-14 20:43:55.698352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "825bcbed67a0"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
