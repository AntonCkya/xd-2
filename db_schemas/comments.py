from pydantic import BaseModel
from datetime import datetime


class Comment (BaseModel):
    movie_id: int
    user_id: int
    text: str
    publication_date: datetime


class Comment_Rating (BaseModel):
    user_id: int
    comment_id: int
    rate: int
