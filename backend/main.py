from fastapi import FastAPI
from backend.database import Base, engine
from backend import models
from backend.routes import users, projects, tasks
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
Base.metadata.create_all(bind=engine)
app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)

@app.get("/")
def home():
    return {"Auth system ready"}
@app.get("/")
def root():
    return {"message": "Backend is running"}

