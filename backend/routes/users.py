from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend import models


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(email: str, password: str, db: Session = Depends(get_db)):
    print("PASSWORD:", password)
    print("LENGTH:", len(password))

    user = models.User(email=email, password=password)
    db.add(user)
    db.commit()
    return {"message": "User created"}

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()

    if not user or password != user.password:

        return {"error": "Invalid credentials"}
    

    return {"message": "Login successful"}