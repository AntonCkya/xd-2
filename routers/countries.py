from fastapi import APIRouter

import utils.movies as movie_utils

from db_schemas.movies import Country as country_schema

from datetime import date

router = APIRouter(
    prefix="/country",
    tags=["country"]
)


# Country
@router.get('/get/movie/')
async def get_country_by_movie(movie_id: int):
    res = movie_utils.get_all_movie_countries(movie_id)
    if res == None or res == []:
        return {"204": "No Content"}
    res_country = []
    for i in res:
        res_country.append(movie_utils.get_country(i[1])[1])
    return res_country
