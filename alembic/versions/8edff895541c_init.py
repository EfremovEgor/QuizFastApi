"""init

Revision ID: 8edff895541c
Revises: 
Create Date: 2023-05-20 18:11:13.891512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8edff895541c"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "questions",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("question_text", sa.String, nullable=False),
        sa.Column("answer_text", sa.String, nullable=False),
        sa.Column("creation_date", sa.DateTime),
    )


def downgrade() -> None:
    op.drop_table("questions")
