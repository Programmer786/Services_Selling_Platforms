"""empty message

Revision ID: 1ad0aab45c78
Revises: b5849e4c317b
Create Date: 2024-09-10 16:21:48.984460

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1ad0aab45c78'
down_revision = 'b5849e4c317b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('msg_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('sender_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('receiver_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('sender_type', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('receiver_type', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('message', mysql.TEXT(), nullable=False),
    sa.Column('timestamp', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('msg_id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
