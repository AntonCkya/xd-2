from fastapi import APIRouter

from datetime import date

import utils.users as user_utils

from db_schemas.users import User as user_schema

import hashlib

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# User
@router.post('/create/')
async def create_user(user: user_schema):
    user_utils.create_user(user)
    return {"200" : "OK"}


@router.get('/get/')
async def get_user(id: int):
    res = user_utils.get_user(id)
    if res != None:
        return res
    return {"204": "No Content"}


@router.get('/get/name/')
async def get_user_by_name(name: str):
    res = user_utils.get_user_by_name(name)
    if res != None:
        return res
    return {"204": "No Content"}


@router.get('/get/email/')
async def get_user_by_email(email: str):
    res = user_utils.get_user_by_email(email)
    if res != None:
        return res
    return {"204": "No Content"}


@router.get('/compare/')
async def compare_user_pass(id: int, password: str):
    user = user_utils.get_user(id)
    if user != None:
        hashpass_obj = hashlib.sha256(bytes(password, 'utf-8'))
        if user[4] == hashpass_obj.hexdigest():
            return {"Compare": "True"}
        else:
            return {"Compare": "False"}
    return {"204": "No Content"}

@router.get('/rating/get/')
async def get_user_rates(id: int):
    res = user_utils.get_user_rates(id)
    if res != None and res != []:
        return res
    return {"204": "No Content"}


@router.put('/update/rating/')
async def update_movie_rating(id_user: int, id_movie: int, rate: int):
    user_utils.update_movie_rating(id_user, id_movie, rate)
    return {"200" : "OK"}
