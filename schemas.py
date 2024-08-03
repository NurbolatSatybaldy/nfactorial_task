from pydantic import BaseModel


class Movie(BaseModel):
    name: str


class User(BaseModel):
    name: str


class Ticket(BaseModel):
    user_id: int
    movie_id: int
