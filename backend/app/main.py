from fastapi import FastAPI
from app.routes.tasks import router as task_router
from app.db.db import get_db, init_db
from datetime import date
from app.routes.updates import router as update_router

app=FastAPI(title="Task Manager")
init_db()
app.include_router(task_router)
app.include_router(update_router)

@app.get("/")
def root():
    return{"message":"Successfully loaded"}
