from sqlalchemy import (
    Table,
    Column,
    Integer,
    Text,
    DateTime,
    ForeignKey
)
from datetime import date, datetime
from models.db_engine import engine, metadata

"""
Таблица Comment:
id - id комментария
movie_id - id фильма, для которого оставили комментарий
user_id - id пользователя, оставившего комментарий
user_name - никнейм пользователя, оставившего комментарий
text - текст комментария
publication_date - дата и время публикации (задается на стороне клиента)

Comment_Rating - таблица, хранящая каждую оценку комментария от каждого пользователя (либо там будет 1/-1, либо как с фильмами)
"""

Comment = Table('comment', metadata,
    Column('id', Integer(), nullable=False, unique=True, primary_key=True, autoincrement=True),
    Column('movie_id', ForeignKey('movie.id'), nullable=False, primary_key=True),
    Column('user_id', ForeignKey('my_user.id'), nullable=False, primary_key=True),
    Column('user_name', ForeignKey('my_user.name'), nullable=False, primary_key=True),
    Column('text', Text(), nullable=False),
    Column('publication_date', DateTime(), nullable=False)
)

Comment_Rating = Table('comment_rating', metadata,
    Column('user_id', ForeignKey('my_user.id'), nullable=False, primary_key=True),
    Column('comment_id', ForeignKey('comment.id'), nullable=False, primary_key=True),
    Column('rate', Integer(), nullable=False)
)
