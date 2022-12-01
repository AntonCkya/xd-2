from fastapi import APIRouter

import utils.movies as movie_utils

from db_schemas.movies import Genre as genre_schema

from datetime import date

router = APIRouter(
    prefix="/genre",
    tags=["genre"]
)


# Genre
@router.get('/get/movie/')
async def get_genre_by_movie(movie_id: int):
    res = movie_utils.get_all_movie_genres(movie_id)
    if res == None or res == []:
        return {"204": "No Content"}
    res_genre = []
    for i in res:
        res_genre.append(movie_utils.get_genre(i[1])[1])
    return res_genre