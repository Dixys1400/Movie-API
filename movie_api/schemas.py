from pydantic import BaseModel
from typing import Optional


class MovieBase(BaseModel):
    title: str
    director: Optional[str] = None
    year: Optional[int] = None
    watched: bool = False


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    pass

class MovieOut(MovieBase):
    id: int

    class Config:
        orm_mode = True
