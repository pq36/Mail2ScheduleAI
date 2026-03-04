from pydantic import BaseModel
from typing import Optional, List

class Task(BaseModel):
    task: str
    date: Optional[str]
    time: Optional[str]
    priority: Optional[str]

class TaskList(BaseModel):
    tasks: List[Task]