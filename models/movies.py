from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Text,
    Date,
    DateTime,
    ForeignKey
)
from datetime import date, datetime
from models.db_engine import engine

"""
Таблица Movie:
id - id фильма из Кинопоиска
title - Название фильма
description - Описание фильма
cover - URL Ссылка на изображение (постер)
premiere_date - Дата выхода фильма (YYYY-MM-DD)
producer - Режиссёр
popularity - Популярность (параметр зависит от частоты заходов на страницу фильма или как-то ещё хз, как Никита решит)

Таблицы Country и Genre содержат списки стран и жанров соответственно (с закрепленными за ними id)

Таблицы Movie_Country и Movie_Genre служат для связи many-to-many между таблицами фильмов и стран/жанров
У каждого фильма может быть несколько жанров и стран производства

Таблицы ниже для Юзеров, комментов, и рейтингов фильмов и комментов
"""

metadata = MetaData()

Movie = Table('movie', metadata, 
    Column('id', Integer(), nullable=False, unique=True, primary_key=True),
    Column('title', String(127), nullable=False, primary_key=True),
    Column('description', Text(), nullable=False),
    Column('cover', String(255), nullable=False),
    Column('premiere_date',Date(), nullable=False),
    Column('producer', String(127), nullable=False),
    Column('popularity', Integer(), nullable=False)
)

Country = Table('country', metadata,
    Column('id', Integer(), nullable=False, unique=True, primary_key=True, autoincrement=True),
    Column('country', String(127), nullable=False, primary_key=True, unique=True)
)

Genre = Table('genre', metadata,
    Column('id', Integer(), nullable=False, unique=True, primary_key=True, autoincrement=True),
    Column('genre', String(127), nullable=False, primary_key=True, unique=True)
)

Movie_Country = Table('movie_country', metadata,
    Column('movie_id', ForeignKey('movie.id'), nullable=False, primary_key=True),
    Column('country_id', ForeignKey('country.id'), nullable=False, primary_key=True)
)

Movie_Genre = Table('movie_genre', metadata,
    Column('movie_id', ForeignKey('movie.id'), nullable=False, primary_key=True),
    Column('genre_id', ForeignKey('genre.id'), nullable=False, primary_key=True)
)

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

Comment = Table('comment', metadata,
    Column('id', Integer(), nullable=False, unique=True, primary_key=True, autoincrement=True),
    Column('movie_id', ForeignKey('movie.id'), nullable=False, primary_key=True),
    Column('user_id', ForeignKey('my_user.id'), nullable=False, primary_key=True),
    Column('text', Text(), nullable=False),
    Column('publication_date', DateTime(), nullable=False)
)

Comment_Rating = Table('comment_rating', metadata,
    Column('user_id', ForeignKey('my_user.id'), nullable=False, primary_key=True),
    Column('comment_id', ForeignKey('comment.id'), nullable=False, primary_key=True),
    Column('rate', Integer(), nullable=False)
)

metadata.create_all(engine)
