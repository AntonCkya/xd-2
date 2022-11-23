from sqlalchemy import insert, values, select, update, and_, desc

from datetime import datetime

from db_schemas.comments import Comment as comment_schema
from db_schemas.comments import Comment_Rating as rating_schema

from models.db_engine import engine
from models.movies import Comment, Comment_Rating


#Comment
def create_comment(comment: comment_schema):
    ins = insert(Comment).values(
        movie_id = comment.movie_id,
        user_id = comment.user_id,
        text = comment.text,
        publication_date = comment.publication_date
    )
    conn = engine.connect()
    r = conn.execute(ins)
    return r


def get_comment_movie (id: int):
    sel = select([Comment]).where(Comment.c.movie_id == id)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchall()


def get_comment_user (id: int):
    sel = select([Comment]).where(Comment.c.user_id == id)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchall()


# Comment_Rating
def create_comment_rating (id_user: int, id_comment: int, rate: int):
    ins = insert(Comment_Rating).values(
        user_id = id_user,
        comment_id = id_comment,
        rate = rate
    )
    conn = engine.connect()
    r = conn.execute(ins)
    return r


def get_comment_rating (id_user: int, id_comment: int):
    sel = select([Comment_Rating]).where(
        and_(
            Comment_Rating.c.user_id == id_user,
            Comment_Rating.c.comment_id == id_comment,
        )
    )
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchone()


def get_comment_rates (id: int):
    sel = select([Comment_Rating]).where(Comment_Rating.c.comment_id == id)
    conn = engine.connect()
    r = conn.execute(sel)
    return r.fetchall()


def update_comment_rating (id_user: int, id_comment: int, rate: int):
    upd = update(Comment_Rating).where(
            and_(
                Comment_Rating.c.user_id == id_user,
                Comment_Rating.c.comment_id == id_comment,
            )
        ).values(rate = rate,)
    conn = engine.connect()
    r = conn.execute(upd)
    return r
