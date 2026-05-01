from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend import models
from datetime import datetime
from backend.auth import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Task
@router.post("/tasks")
def create_task(title: str, description: str, project_id: int, assigned_to: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    task = models.Task(title=title, description=description, status="Todo", project_id=project_id, assigned_to=assigned_to, user_id=current_user.id)
    db.add(task)
    db.commit()
    return {"message": "Task created"}

# Get Tasks
@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Task).filter(models.Task.user_id == current_user.id).all()

# Update Task Status
@router.put("/tasks/{task_id}")
def update_task(task_id: int, status: str, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        return {"message": "Task not found"}
    
    task.status = status
    db.commit()
    return {"message": "Task updated"}
@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()

    total = len(tasks)
    completed = len([t for t in tasks if t.status == "Done"])
    pending = len([t for t in tasks if t.status != "Done"])

    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending
    }
