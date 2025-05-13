from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Task Manager!"}

from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
tasks = []

from fastapi import FastAPI
from typing import List

app = FastAPI()

# Define the task model
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

tasks = []  # In-memory storage

# Create a task
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

# Get all tasks
@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks

# Get a task by id
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

# Update a task
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = task
    return task

# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks.pop(task_id)
    return {"message": "Task deleted successfully"}
