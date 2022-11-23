from pydantic import BaseModel, EmailStr, validator
from datetime import datetime


class User(BaseModel):
    name: str
    email: EmailStr
    registration_date: datetime
    password: str
    
    @validator('password')
    def password_validator(cls, password):
        numlist = list('0123456789')
        literlist = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')

        hasDigit = False
        hasLiter = False

        for i in list(password):
            if i in numlist:
                hasDigit = True
            if i in literlist:
                hasLiter = True

        if not hasDigit:
            raise ValueError('passwords does not contain a number')
        if not hasDigit:
            raise ValueError('passwords does not contain a latin letter')
        if len(password) < 8:
            raise ValueError('password length less than 8')
        return password


class Movie_Rating(BaseModel):
    movie_id: int
    user_id: int
    rate: int
