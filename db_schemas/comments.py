from pydantic import BaseModel
from datetime import datetime


class Comment (BaseModel):
    """
    class Comment
    Модель для валидации комментариев pydantic

    movie_id - id фильма, к которому написан комментарий
    user_id - id пользователя, написавшего комментарий
    user_name - имя пользователя
    text - текст комментария
    publication_date - дата и время публикации
    """

    movie_id: int
    user_id: int
    user_name: str
    text: str
    publication_date: datetime


class Comment_Rating (BaseModel):
    """
    class Comment_Rating
    Модель для валидации оценок к комментариям

    user_id - id пользователя, оценившего комментарий
    comment_id - id комментария
    rate - оценка (число)
    """

    user_id: int
    comment_id: int
    rate: int
