"""complete posts table

Revision ID: 374469f39177
Revises: de3802d43132
Create Date: 2023-06-14 21:15:33.652520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "374469f39177"
down_revision = "de3802d43132"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="True"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
