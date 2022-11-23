from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

from datetime import date

import utils.movies as movie_utils
import utils.users as user_utils
import utils.comments as comment_utils

from db_schemas.movies import Movie as movie_schema
from db_schemas.movies import Country as country_schema
from db_schemas.movies import Genre as genre_schema
from db_schemas.movies import Movie_all as movie_all_schema

from db_schemas.users import User as user_schema
from db_schemas.users import Movie_Rating as movie_rating_schema

from db_schemas.comments import Comment as comment_schema
from db_schemas.comments import Comment_Rating as comment_rating_schema

from db_schemas.movies import movie_all_to_genres, movie_all_to_countries, movie_all_to_movie

import hashlib

app = FastAPI()

origins = [
    "http://localhost"
    "https://localhost",
    "http://localhost:8000",
    "https://localhost:8000",
    "http://localhost:3000",
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# root
@app.get('/', tags=["root"])
async def test():
	return {"xd": "api"}


# Movie
@app.post('/movie/create/', tags=["movie"])
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
	

@app.get('/movie/get/', tags=["movie"])
async def get_movie(id: int):
    res = movie_utils.get_movie(id)
    if res != None:
        return res
    return {"204": "No Content"}


@app.get('/movie/get/prod/', tags=["movie"])
async def get_movie_by_producer(prod: str):
    res = movie_utils.get_all_by_prod(prod)
    if res != None and res != []:
        return res
    return {"204": "No Content"}


@app.get('/movie/get/all/pop', tags=["movie"])
async def get_movie_by_popularity():
    res = movie_utils.get_all_by_pop()
    if res != None:
        return res
    return {"204": "No Content"}


@app.get('/movie/get/date/', tags=["movie"])
async def get_movie_in_date(date_1: date, date_2: date):
    res = movie_utils.get_all_in_date(date_1, date_2)
    if res != None and res != []:
        return res
    return {"204": "No Content"}


@app.get('/movie/get/all', tags=["movie"])
async def get_movie_all():
    res = movie_utils.get_all()
    if res != None:
        return res
    return {"204": "No Content"}


@app.get('/movie/get/country/', tags=["movie"])
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


@app.get('/movie/get/genre/', tags=["movie"])
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


@app.put('/movie/update/popularity/', tags=["movie"])
async def update_popularity(id: int, pop: int):
    movie_utils.update_pop(id, pop)
    return {"200" : "OK"}


# Country
@app.get('/country/get/movie/', tags=["country"])
async def get_country_by_movie(movie_id: int):
    res = movie_utils.get_all_movie_countries(movie_id)
    if res == None or res == []:
        return {"204": "No Content"}
    res_country = []
    for i in res:
        res_country.append(movie_utils.get_country(i[1])[1])
    return res_country


# Genre
@app.get('/genre/get/movie/', tags=["genre"])
async def get_genre_by_movie(movie_id: int):
    res = movie_utils.get_all_movie_genres(movie_id)
    if res == None or res == []:
        return {"204": "No Content"}
    res_genre = []
    for i in res:
        res_genre.append(movie_utils.get_genre(i[1])[1])
    return res_genre


# User
@app.post('/user/create/', tags=["user"])
async def create_user(user: user_schema):
    user_utils.create_user(user)
    return {"200" : "OK"}


@app.get('/user/get/', tags=["user"])
async def get_user(id: int):
    res = user_utils.get_user(id)
    if res != None:
        return res
    return {"204": "No Content"}


@app.get('/user/get/name/', tags=["user"])
async def get_user_by_name(name: str):
    res = user_utils.get_user_by_name(name)
    if res != None:
        return res
    return {"204": "No Content"}


@app.get('/user/get/email/', tags=["user"])
async def get_user_by_email(email: str):
    res = user_utils.get_user_by_email(email)
    if res != None:
        return res
    return {"204": "No Content"}


@app.get('/user/compare/', tags=["user"])
async def compare_user_pass(id: int, password: str):
    user = user_utils.get_user(id)
    if user != None:
        hashpass_obj = hashlib.sha256(bytes(password, 'utf-8'))
        if user[4] == hashpass_obj.hexdigest():
            return {"Compare": "True"}
        else:
            return {"Compare": "False"}
    return {"204": "No Content"}


# Movie_Rating
@app.post('/movie/rating/create/', tags=["movie"])
async def create_movie_rating(id_user: int, id_movie: int, rate: int):
    user_utils.create_movie_rating(id_user, id_movie, rate)
    return {"200" : "OK"}


@app.get('/movie/rating/get/', tags=["movie"])
async def get_movie_rates(id: int):
    res = user_utils.get_movie_rates(id)
    if res != None and res != []:
        return res
    return {"204": "No Content"}


@app.get('/user/rating/get/', tags=["user"])
async def get_user_rates(id: int):
    res = user_utils.get_user_rates(id)
    if res != None and res != []:
        return res
    return {"204": "No Content"}


@app.put('/user/update/rating/', tags=["user"])
async def update_movie_rating(id_user: int, id_movie: int, rate: int):
    user_utils.update_movie_rating(id_user, id_movie, rate)
    return {"200" : "OK"}


# Comment
@app.post('/comment/create/', tags=["comment"])
async def create_comment(comment: comment_schema):
    comment_utils.create_comment(comment)
    return {"200" : "OK"}


@app.get('/comment/get/movie/', tags=["comment"])
async def get_comment_movie(id: int):
    res = comment_utils.get_comment_movie(id)
    if res != None and res != []:
        return res
    return {"204": "No Content"}


@app.get('/comment/get/user/', tags=["comment"])
async def get_comment_user(id: int):
    res = comment_utils.get_comment_user(id)
    if res != None and res != []:
        return res
    return {"204": "No Content"}


# Comment_Rating
@app.post('/comment/rating/create/', tags=["comment"])
async def create_comment_rating(id_user: int, id_comment: int, rate: int):
    comment_utils.create_comment_rating(id_user, id_comment, rate)
    return {"200" : "OK"}


@app.get('/comment/rating/get/', tags=["comment"])
async def get_comment_rating(id_user: int, id_comment: int):
    res = comment_utils.get_comment_rating(id_user, id_comment)
    if res != None and res != []:
        return res
    return {"204": "No Content"}


@app.get('/comment/rating/raters_of_comment/', tags=["comment"])
async def get_comment_rates(id: int):
    res = comment_utils.get_comment_rates(id)
    if res != None and res != []:
        return res
    return {"204": "No Content"}


@app.put('/comment/rating/update/', tags=["comment"])
async def update_comment_rating(id_user: int, id_comment: int, rate: int):
    comment_utils.update_comment_rating(id_user, id_comment, rate)
    return {"200" : "OK"}


def custom_openapi():
	if app.openapi_schema:
		return app.openapi_schema
	openapi_schema = get_openapi(
    	title="[ xd ]",
		version="0.0.1",
		description="API к онлайн-кинотеатру [ xd ]",
		routes=app.routes,
	)
	app.openapi_schema = openapi_schema
	return app.openapi_schema

app.openapi = custom_openapi
