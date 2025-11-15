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




CSV_FIELDS = ["id", "title", "description", "priority", "done"]

class ToDoList:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task_id: str) -> bool:
        t = self.find_task_by_id(task_id)
        if t:
            self.tasks.remove(t)
            return True
        return False

    def mark_done(self, task_id: str) -> bool:
        t = self.find_task_by_id(task_id)
        if t:
            t.done = True
            return True
        return False

    def find_task_by_id(self, task_id: str) -> Optional[Task]:
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None

    def list_tasks(self, show_all=True) -> List[Task]:
        if show_all:
            return list(self.tasks)
        return [t for t in self.tasks if not t.done]

    def save_to_csv(self, filepath: str):
        with open(filepath, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
            writer.writeheader()
            for t in self.tasks:
                row = asdict(t)
                row["done"] = str(row["done"])
                writer.writerow(row)

    def load_from_csv(self, filepath: str):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.tasks = []
                for row in reader:
                    # تبدیل مقدار done به بولین
                    done = row.get("done", "False").strip().lower() in ("true", "1", "yes")
                    task = Task(
                        id=row.get("id"),
                        title=row.get("title", ""),
                        description=row.get("description", ""),
                        priority=row.get("priority", "low").lower(),
                        done=done
                    )
                    self.tasks.append(task)
        except FileNotFoundError:
            # اگر فایل وجود ندارد، لیست خالی می‌ماند
            self.tasks = []
