"""add foreign key to posts table

Revision ID: de3802d43132
Revises: 6c35afc253c5
Create Date: 2023-06-14 21:11:18.566201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "de3802d43132"
down_revision = "6c35afc253c5"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
