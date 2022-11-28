from pydantic import BaseModel, EmailStr, validator
from datetime import datetime


class User(BaseModel):
    name: str
    email: EmailStr
    registration_date: datetime
    password: str
    
    #Валидатор на длину пароля (8+)
    @validator('password')
    def password_validator(cls, password):
        if len(password) < 8:
            raise ValueError('password length less than 8')
        return password


class Movie_Rating(BaseModel):
    movie_id: int
    user_id: int
    rate: int
