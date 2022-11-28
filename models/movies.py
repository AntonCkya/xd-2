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
from models.db_engine import engine, metadata

"""
Таблица Movie:
id - id фильма из Кинопоиска
title - Название фильма
description - Описание фильма
cover - URL Ссылка на изображение (постер)
premiere_date - Дата выхода фильма (YYYY-MM-DD)
producer - Режиссёр
popularity - Популярность (параметр зависит от частоты заходов на страницу фильма или как-то ещё хз, как Никита решит)
age - разрешенный для просмотра возраст

Таблицы Country и Genre содержат списки стран и жанров соответственно (с закрепленными за ними id)

Таблицы Movie_Country и Movie_Genre служат для связи many-to-many между таблицами фильмов и стран/жанров
У каждого фильма может быть несколько жанров и стран производства
"""

Movie = Table('movie', metadata, 
    Column('id', Integer(), nullable=False, unique=True, primary_key=True),
    Column('title', String(127), nullable=False, primary_key=True),
    Column('description', Text(), nullable=False),
    Column('cover', String(255), nullable=False),
    Column('premiere_date',Date(), nullable=False),
    Column('producer', String(127), nullable=False),
    Column('popularity', Integer(), nullable=False),
    Column('age', Integer(), nullable=False),
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
