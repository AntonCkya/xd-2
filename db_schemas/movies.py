from pydantic import BaseModel, HttpUrl
from datetime import date
from typing import List


class Movie (BaseModel):
    id: int
    title : str
    description : str
    cover : HttpUrl
    premiere_date : date
    producer : str
    popularity : int
    age : int


class Country (BaseModel):
    country: str


class Genre (BaseModel):
    genre: str


# Схема для получения у фильма вместе с ним его страны и жанры
class Movie_all (BaseModel):
    id: int
    title : str
    description : str
    cover : HttpUrl
    premiere_date : date
    producer : str
    popularity : int
    age : int
    country : List[str]
    genre : List[str]


#Адаптеры movie_all в вид movie или извлечение оттуда жанров/стран
def movie_all_to_movie (movie_all: Movie_all) -> Movie:
    movie = Movie(
        id = movie_all.id,
        title = movie_all.title,
        description = movie_all.description,
        cover = movie_all.cover,
        premiere_date = movie_all.premiere_date,
        producer = movie_all.producer,
        popularity = movie_all.popularity,
        age = movie_all.age
    )
    return movie


def movie_all_to_countries (movie_all: Movie_all) -> List[str]:
    return movie_all.country


def movie_all_to_genres (movie_all: Movie_all) -> List[str]:
    return movie_all.genre
