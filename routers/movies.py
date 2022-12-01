from fastapi import APIRouter

import utils.movies as movie_utils
import utils.users as user_utils

from db_schemas.movies import Movie as movie_schema
from db_schemas.movies import Country as country_schema
from db_schemas.movies import Genre as genre_schema
from db_schemas.movies import Movie_all as movie_all_schema

from db_schemas.movies import movie_all_to_genres, movie_all_to_countries, movie_all_to_movie

from datetime import date

router = APIRouter(
    prefix="/movie",
    tags=["movie"]
)


# Movie
@router.post('/create/')
async def create_movie(movie: movie_all_schema):
    movie_utils.create_movie(movie_all_to_movie(movie))
    for i in movie_all_to_countries(movie):
        country = country_schema(country= i)
        movie_utils.create_country(country)
        movie_utils.create_movie_country(movie.id, movie_utils.get_country_by_name(i)[0])
    for i in movie_all_to_genres(movie):
        genre = genre_schema(genre= i)
        movie_utils.create_genre(genre)
        movie_utils.create_movie_genre(movie.id, movie_utils.get_genre_by_name(i)[0])
    return {"200" : "OK"}
	

@router.get('/get/')
async def get_movie(id: int):
    res = movie_utils.get_movie(id)
    if res != None:
        return res
    return {"204": "No Content"}


@router.get('/get/prod/')
async def get_movie_by_producer(prod: str):
    res = movie_utils.get_all_by_prod(prod)
    if res != None and res != []:
        return res
    return {"204": "No Content"}


@router.get('/get/all/pop')
async def get_movie_by_popularity():
    res = movie_utils.get_all_by_pop()
    if res != None:
        return res
    return {"204": "No Content"}


@router.get('/get/date/')
async def get_movie_in_date(date_1: date, date_2: date):
    res = movie_utils.get_all_in_date(date_1, date_2)
    if res != None and res != []:
        return res
    return {"204": "No Content"}


@router.get('/get/all')
async def get_movie_all():
    res = movie_utils.get_all()
    if res != None:
        return res
    return {"204": "No Content"}


@router.get('/get/title/')
async def get_movie_by_title(name: str):
    res = movie_utils.get_movie_by_name(name)
    if res != None:
        return res
    return {"204": "No Content"}


@router.get('/get/country/')
async def get_movie_by_country(country: str):
    cntr = movie_utils.get_country_by_name(country)
    if cntr == None:
        return {"204": "No Content"}
    id = cntr[0]
    res = movie_utils.get_all_country_movies(id)
    if res == None:
        return {"204": "No Content"}
    res_movie = []
    for i in res:
        res_movie.append(movie_utils.get_movie(i[0]))
    return res_movie


@router.get('/get/genre/')
async def get_movie_by_genre(genre: str):
    gnr = movie_utils.get_genre_by_name(genre)
    if gnr == None:
        return {"204": "No Content"}
    id = gnr[0]
    res = movie_utils.get_all_genre_movies(id)
    if res == None:
        return {"204": "No Content"}
    res_movie = []
    for i in res:
        res_movie.append(movie_utils.get_movie(i[0]))
    return res_movie


@router.put('/update/popularity/')
async def update_popularity(id: int, pop: int):
    movie_utils.update_pop(id, pop)
    return {"200" : "OK"}


@router.post('/rating/create/')
async def create_movie_rating(id_user: int, id_movie: int, rate: int):
    user_utils.create_movie_rating(id_user, id_movie, rate)
    return {"200" : "OK"}


@router.get('/rating/get/')
async def get_movie_rates(id: int):
    res = user_utils.get_movie_rates(id)
    if res != None and res != []:
        return res
    return {"204": "No Content"}
