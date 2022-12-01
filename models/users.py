from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)
from datetime import date, datetime
from models.db_engine import engine, metadata

"""
Таблица User:
id - id юзера
name - никнейм пользователя
email - email пользователя (str@str.str)
registration_date - дата и время регистрации (задается на стороне клиента)
hashpass - захешированный пароль

Movie_Rating - таблица, хранящая каждую оценку фильма от каждого пользователя
"""

User = Table('my_user', metadata,
    Column('id', Integer(), nullable=False, unique=True, primary_key=True, autoincrement=True),
    Column('name', String(127), nullable=False, primary_key=True, unique=True),
    Column('email', String(255), nullable=False, unique=True),
    Column('registration_date', DateTime(), nullable=False),
    Column('hashpass', String(255), nullable=False),
)

Movie_Rating = Table('movie_rating', metadata,
    Column('movie_id', ForeignKey('movie.id'), nullable=False, primary_key=True),
    Column('user_id', ForeignKey('my_user.id'), nullable=False, primary_key=True),
    Column('rate', Integer(), nullable=False)
)
