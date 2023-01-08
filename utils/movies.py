from sqlalchemy import insert, values, select, update, and_, desc

from datetime import date

from db_schemas.movies import Movie as movie_schema
from db_schemas.movies import Country as country_schema
from db_schemas.movies import Genre as genre_schema

from models.db_engine import engine
from models.movies import Movie, Country, Genre, Movie_Country, Movie_Genre

"""
Модуль для работы с фильмами и их оценками в базе данных

Movie:

create_movie - создать фильм
get_movie - получить фильм по id
update_pop - изменить популярность фильма по id
get_all - получить все фильмы
get_all_by_pop - получить все фильмы, отсортированные по популярности
get_all_by_prod - получить все фильмы от данного режиссера
get_all_in_date - получить все фильмы, вышедшие между date1 и date2
get_movie_by_name - получить фильм по названию


Country:

create_country - создать страну
get_country - получить страну по id
get_country_by_name - получить страну по названию
get_all_countries - получить все страны


Movie_Country:

create_movie_country - создать зависимость фильм-страна
get_all_movie_countries - получить все зависимости с данным id фильма
get_all_country_movies - получить все зависимости с данным id страны


Genre:

create_genre - создать жанр
get_genre - получить жанр по id
get_genre_by_name - получить жанр по названию
get_all_genres - получить все жанры


Movie_Genre:

create_movie_genre - создать зависимость фильм-жанр
get_all_movie_genres - получить все зависимости с данным id фильма
get_all_genre_movies - получить все зависимости с данным id жанра
"""

# Movie
def create_movie (movie: movie_schema):
    ins = Movie.insert().values(
        id = movie.id,
        title = movie.title,
        description = movie.description,
        cover = movie.cover,
        premiere_date = movie.premiere_date,
        producer = movie.producer,
        popularity = movie.popularity,
        age = movie.age
    )
    conn = engine.connect()
    r = conn.execute(ins)
    return r


def get_movie (id: int):
    sel = select([Movie]).where(Movie.c.id == id)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchone()


def update_pop (id: int, pop: int):
    upd = update(Movie).where(Movie.c.id == id).values(popularity = pop,)
    conn = engine.connect()
    r = conn.execute(upd)
    return r


def get_all ():
    sel = select([Movie])
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchall()


def get_all_by_pop():
    sel = select([Movie]).order_by(desc(Movie.c.popularity))
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchall()


def get_all_by_prod(prod: str):
    sel = select([Movie]).where(Movie.c.producer == prod)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchall()


def get_all_in_date(date_1: date, date_2: date):
    sel = select([Movie]).where(
        and_(
            Movie.c.premiere_date >= date_1,
            Movie.c.premiere_date <= date_2
            )
        )
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchall()


def get_movie_by_name(name: str):
    sel = select([Movie]).where(Movie.c.title.like("%{name}%".format(name=name)))
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchall()


# Country
def create_country (country: country_schema):
    sel = select([Country]).where(Country.c.country == country.country)
    conn = engine.connect()
    r = conn.execute(sel)
    if r.fetchone() == None: 
        ins = insert(Country).values(
            country = country.country
        )
        r = conn.execute(ins)
    return r


def get_country (id: int):
    sel = select([Country]).where(Country.c.id == id)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchone()


def get_country_by_name (name: str):
    sel = select([Country]).where(Country.c.country == name)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchone()


def get_all_countries ():
    sel = select([Country])
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchall()


# Movie_Country
def create_movie_country (id_movie: int, id_country: int):
    ins = insert(Movie_Country).values(
        movie_id = id_movie,
        country_id = id_country
    )
    conn = engine.connect()
    r = conn.execute(ins)
    return r


def get_all_movie_countries (id_movie: int):
    sel = select([Movie_Country]).where(Movie_Country.c.movie_id == id_movie)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchall()


def get_all_country_movies (id_country: int):
    sel = select([Movie_Country]).where(Movie_Country.c.country_id == id_country)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchall()


# Genre
def create_genre (genre: genre_schema):
    sel = select([Genre]).where(Genre.c.genre == genre.genre)
    conn = engine.connect()
    r = conn.execute(sel)
    if r.fetchone() == None:
        ins = insert(Genre).values(
            genre = genre.genre
        )
        r = conn.execute(ins)
    return r


def get_genre (id: int):
    sel = select([Genre]).where(Genre.c.id == id)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchone()


def get_genre_by_name (name: str):
    sel = select([Genre]).where(Genre.c.genre == name)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchone()


def get_all_genres ():
    sel = select([Genre])
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchall()


# Movie_Genre
def create_movie_genre (id_movie: int, id_genre: int):
    ins = insert(Movie_Genre).values(
        movie_id = id_movie,
        genre_id = id_genre
    )
    conn = engine.connect()
    r = conn.execute(ins)
    return r


def get_all_movie_genres (id_movie: int):
    sel = select([Movie_Genre]).where(Movie_Genre.c.movie_id == id_movie)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchall()


def get_all_genre_movies (id_genre: int):
    sel = select([Movie_Genre]).where(Movie_Genre.c.genre_id == id_genre)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchall()
