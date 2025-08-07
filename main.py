from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app= FastAPI()

class task_model(BaseModel):
    id: int
    name: str
    description: Optional[str]= None

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
#TODO: Implement a way to delete tasks
#TODO: Implement a way to update tasks
#ToDO: Implement a way to mark tasks as completed
#TODO: Implement a way to save tasks in a database