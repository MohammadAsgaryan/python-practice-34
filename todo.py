from dataclasses import dataclass, asdict
import csv
from typing import List, Optional
import uuid



@dataclass
class Task:
    id: str
    title: str
    description: str
    priority: str
    done: bool = False
    
    
    
    
@classmethod
def create(cls, title: str, description: str, priority: str):
    return cls(
        id = str(uuid.uuid4()),
        title = title.strip(),
        description = description.strip(),
        priority = priority.strip().lower,
        done = False
    )
