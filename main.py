from fastapi import FastAPI, Depends
import schemas
import models
from db import engine, SessionLocal
from sqlalchemy.orm import Session
app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.post('/')
def home(request: schemas.User, db: Session = Depends(get_db)):
    new_blog = models.User(username=request.username, email=request.email, password=request.password, cart=request.cart, profileImage=request.profileImage, profileImageName=request.profileImageName, isActive=request.isActive, emailVerified=request.emailVerified) 
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
