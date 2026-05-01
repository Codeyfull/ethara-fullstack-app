from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database import Base
from backend import models

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    owner_id = Column(Integer)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    status = Column(String, default="Todo")
    project_id = Column(Integer) 
    assigned_to = Column(Integer)

class ProjectUser(Base):
    __tablename__ = "project_users"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer)
    user_id = Column(Integer)
    role = Column(String) # user
    
