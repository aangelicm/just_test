from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_methods=["*"],
)

# Зависимость для БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/auth/user", response_model=schemas.UserResponse)
def handle_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(
        models.User.username == user_data.username
    ).first()
    
    if user:
        return user
    else:
        new_user = models.User(
            username=user_data.username
            # другие поля если есть
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user