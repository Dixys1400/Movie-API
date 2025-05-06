from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from movie_api import models, schemas
from movie_api import database

router = APIRouter(prefix="/movies", tags=["Movies"])


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/", response_model=schemas.MovieOut)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


@router.get("/", response_model=list[schemas.MovieOut])
def get_movies(db: Session = Depends(get_db)):
    return db.query(models.Movie).all()


@router.get("/watched", response_model=list[schemas.MovieOut])
def get_watched_movies(db: Session = Depends(get_db)):
    return db.query(models.Movie).filter(models.Movie.watched == True).all()


@router.get("/unwatched", response_model=list[schemas.MovieOut])
def get_unwatched_movies(db: Session = Depends(get_db)):
    return db.query(models.Movie).filter(models.Movie.watched == False).all()


@router.get("/{movie_id}", response_model=schemas.MovieOut)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.put("/{movie_id}", response_model=schemas.MovieOut)
def update_movie(movie_id: int, updated: schemas.MovieUpdate, db: Session = Depends(get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    for key, value in updated.dict(exclude_unset=True).items():
        setattr(movie, key, value)
    db.commit()
    db.refresh(movie)
    return movie


@router.delete("/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(movie)
    db.commit()
    return {"detail": "Movie deleted"}






