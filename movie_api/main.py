from fastapi import FastAPI
from movie_api import models
from movie_api import database
from movie_api.routers import movies

app = FastAPI(title = "🎬 Movie Watchlist API")


models.Base.metadata.create_all(database.engine)


app.include_router(movies.router)



