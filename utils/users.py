from sqlalchemy import insert, values, select, update, and_, desc

from datetime import datetime

from db_schemas.users import User as user_schema
from db_schemas.users import Movie_Rating as rating_schema

from models.db_engine import engine
from models.movies import User, Movie_Rating

import hashlib


# User
def create_user (user: user_schema):
    hashpass_obj = hashlib.sha256(bytes(user.password, 'utf-8'))
    ins = insert(User).values(
        name = user.name,
        email = user.email,
        registration_date = user.registration_date,
        hashpass = hashpass_obj.hexdigest()
    )
    conn = engine.connect()
    r = conn.execute(ins)
    return r


def get_user (id: int):
    sel = select([User]).where(User.c.id == id)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchone()


def get_user_by_name (name: str):
    sel = select([User]).where(User.c.name.like("%{name}%".format(name=name)))
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchone()


def get_user_by_email (email: str):
    sel = select([User]).where(User.c.email == email)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchone()


# Movie_Rating
def create_movie_rating (id_user: int, id_movie: int, rate: int):
    ins = insert(Movie_Rating).values(
        movie_id = id_movie,
        user_id = id_user,
        rate = rate
    )
    conn = engine.connect()
    r = conn.execute(ins)
    return r


def get_user_rates (id: int):
    sel = select([Movie_Rating]).where(Movie_Rating.c.user_id == id)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchall()


def get_movie_rates (id: int):
    sel = select([Movie_Rating]).where(Movie_Rating.c.movie_id == id)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchall()


def update_movie_rating (id_user: int, id_movie: int, rate: int):
    upd = update(Movie_Rating).where(
            and_(
                Movie_Rating.c.movie_id == id_movie,
                Movie_Rating.c.user_id == id_user
            )
        ).values(rate = rate,)
    conn = engine.connect()
    r = conn.execute(upd)
    return r
