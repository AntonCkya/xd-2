from pydantic import BaseModel, HttpUrl
from datetime import date
from typing import List


class Movie (BaseModel):
    """
    class Movie
    Модель для валидации фильмов

    id - id фильма (раньше использовался id кинопоиска из-за плеера, но щас хз)
    title - название
    description - описание
    cover - URL ссылка на изображение постера к фильму (желательно от кинопоиска, они одного размера)
    premiere_date - дата выхода
    producer - режиссер
    popularity - "популярность" фильма (отчасти осталось после предыдущей версии но возможно найдет применение)
    age - возрастное ограничение
    """

    id: int
    title : str
    description : str
    cover : HttpUrl
    premiere_date : date
    producer : str
    popularity : int
    age : int


class Country (BaseModel):
    """
    class Country
    Модель для валидации страны производства

    country - страна производства (регистрозависимо)
    """

    country: str


class Genre (BaseModel):
    """
    class Genre
    Модель для валидации жанров фильмов

    genre - жанр фильма (регистрозависимо)
    """
    genre: str


class Movie_all (BaseModel):
    """
    class Movie_all
    Модель для валидации общего фильма

    Кроме полей самого фильма имеет массив жанров и массив стран
    Модель создана, чтобы создавать фильм со всеми жанрами и странами одним запросом.
    """

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


def movie_all_to_movie (movie_all: Movie_all) -> Movie:
    """
    Адаптер, преобразующий Movie_all объект в объект Movie
    Отсекает часть со странами и жанрами
    """

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
    """
    Адаптер, преобразующий Movie_all объект в массив стран (как строк)
    """
    return movie_all.country


def movie_all_to_genres (movie_all: Movie_all) -> List[str]:
    """
    Адаптер, преобразующий Movie_all объект в массив жанров (как строк)
    """
    return movie_all.genre
