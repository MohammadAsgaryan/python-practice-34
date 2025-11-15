# To-Do List (Python, OOP, CSV)

Simple To-Do list manager using Python classes and CSV storage.

## Features
- Add, remove and mark tasks as done
- Save and load tasks from `tasks.csv`
- Each task has: id, title, description, priority (high/medium/low), done status
- Simple CLI menu

## How to run
```bash
python app.py

Tasks are automatically loaded from tasks.csv (if exists) and saved on exit.

Files

todo.py — Task and ToDoList classes (CSV save/load)

app.py — Command-line interface (menu)

tasks.csv — task storage (generated)

Notes

No external libraries required.

You can extend it: add due dates, sorting, filtering, priority colors, or GUI.