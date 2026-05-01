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

# Create Project
@router.post("/projects")
def create_project(name: str, description: str, db: Session = Depends(get_db)):
    project = models.Project(name=name, description=description, owner_id=1)
    db.add(project)
    db.commit()
    return {"message": "Project created"}

# Create user
@router.post("/projects/{project_id}/users")
def add_user(project_id: int, user_id: int, role: str, db: Session = Depends(get_db)):
    project_user = models.ProjectUser(project_id=project_id, user_id=user_id, role=role)
    db.add(project_user)
    db.commit()
    return {"message": "User added to project"}

# Get all projects
@router.get("/projects")
def get_projects(db: Session = Depends(get_db)):
    return db.query(models.Project).all()