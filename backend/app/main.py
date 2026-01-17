from fastapi import FastAPI
from app.routes.tasks import router as task_router

app=FastAPI(title="Task Manager")

app.include_router(task_router)

@app.get("/")
def root():
    return{"message":"Successfully loaded"}
