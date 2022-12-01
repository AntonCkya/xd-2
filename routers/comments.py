from fastapi import APIRouter

from db_schemas.comments import Comment as comment_schema
from db_schemas.comments import Comment_Rating as comment_rating_schema

import utils.comments as comment_utils

router = APIRouter(
    prefix="/comment",
    tags=["comment"]
)


# Comment
@router.post('/create/')
async def create_comment(comment: comment_schema):
    comment_utils.create_comment(comment)
    return {"200" : "OK"}


@router.get('/get/movie/')
async def get_comment_movie(id: int):
    res = comment_utils.get_comment_movie(id)
    if res != None and res != []:
        return res
    return {"204": "No Content"}


@router.get('/get/user/')
async def get_comment_user(id: int):
    res = comment_utils.get_comment_user(id)
    if res != None and res != []:
        return res
    return {"204": "No Content"}


# Comment_Rating
@router.post('/rating/create/')
async def create_comment_rating(id_user: int, id_comment: int, rate: int):
    comment_utils.create_comment_rating(id_user, id_comment, rate)
    return {"200" : "OK"}


@router.get('/rating/get/')
async def get_comment_rating(id_user: int, id_comment: int):
    res = comment_utils.get_comment_rating(id_user, id_comment)
    if res != None and res != []:
        return res
    return {"204": "No Content"}


@router.get('/rating/raters_of_comment/')
async def get_comment_rates(id: int):
    res = comment_utils.get_comment_rates(id)
    if res != None and res != []:
        return res
    return {"204": "No Content"}


@router.put('/rating/update/')
async def update_comment_rating(id_user: int, id_comment: int, rate: int):
    comment_utils.update_comment_rating(id_user, id_comment, rate)
    return {"200" : "OK"}
