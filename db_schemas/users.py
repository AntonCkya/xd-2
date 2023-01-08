from pydantic import BaseModel, EmailStr, validator
from datetime import datetime


class User(BaseModel):
    """
    class User
    Модель для валидации пользователей

    name - имя пользователя
    email - адрес электронной почты формата str@str.str
    registration_date - дата и время регистрации
    password - пароль (возможно захешированнный, в любом случае хешируется перед отправкой в БД)
    
    password должен иметь длину минимум 8 символов 
    """

    name: str
    email: EmailStr
    registration_date: datetime
    password: str
    
    @validator('password')
    def password_validator(cls, password):
        if len(password) < 8:
            raise ValueError('password length less than 8')
        return password


class Movie_Rating(BaseModel):
    """
    class Movie_Rating
    Модель для валидации оценок фильмам

    movie_id - id фильма
    user_id - id пользователя
    rate - оценка (число)
    """

    movie_id: int
    user_id: int
    rate: int
