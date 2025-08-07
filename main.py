from asyncio import tasks
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class task_model(BaseModel):
    id: int
    name: str
    description: str

tasks = []

@app.get("/")
def read_root():
    return {"message":"Welcome to the root endpoint!"}


@app.post("/new")
def new_task(task:task_model):
    tasks.append(task)
    return {"message": "Task added successfully", "task": task}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}