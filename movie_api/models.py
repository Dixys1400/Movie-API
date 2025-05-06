from sqlalchemy import Column, Integer, String, Boolean
from movie_api.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    director = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    watched = Column(Boolean, default=True)


