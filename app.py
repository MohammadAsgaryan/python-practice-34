
from todo import ToDoList, Task
import os

CSV_FILE = "tasks.csv"

def print_menu():
    print("\n=== To-Do List Menu ===")
    print("1) Add task")
    print("2) Remove task")
    print("3) Mark task as done")
    print("4) Show tasks")
    print("5) Save tasks")
    print("6) Load tasks")
    print("7) Exit")

def input_priority():
    while True:
        p = input("Priority (high/medium/low): ").strip().lower()
        if p in ("high", "medium", "low"):
            return p
        print("Invalid priority. Choose high, medium or low.")

def show_tasks(todo: ToDoList):
    tasks = todo.list_tasks(show_all=True)
    if not tasks:
        print("No tasks.")
        return
    print(f"\nTotal tasks: {len(tasks)}")
    for i, t in enumerate(tasks, start=1):
        status = "✅" if t.done else "❌"
        print(f"{i}. [{status}] {t.title} (id: {t.id}) - priority: {t.priority}")
        if t.description:
            print(f"    {t.description}")

def main():
    todo = ToDoList()
    # بارگذاری خودکار اگر فایل وجود داشته باشد
    if os.path.exists(CSV_FILE):
        todo.load_from_csv(CSV_FILE)
        print(f"Loaded {len(todo.tasks)} tasks from {CSV_FILE}")

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            title = input("Title: ").strip()
            description = input("Description: ").strip()
            priority = input_priority()
            task = Task.create(title, description, priority)
            todo.add_task(task)
            print("Task added.")
        elif choice == "2":
            task_id = input("Enter task id to remove: ").strip()
            if todo.remove_task(task_id):
                print("Removed.")
            else:
                print("Task id not found.")
        elif choice == "3":
            task_id = input("Enter task id to mark done: ").strip()
            if todo.mark_done(task_id):
                print("Marked as done.")
            else:
                print("Task id not found.")
        elif choice == "4":
            show_tasks(todo)
        elif choice == "5":
            todo.save_to_csv(CSV_FILE)
            print(f"Saved to {CSV_FILE}.")
        elif choice == "6":
            todo.load_from_csv(CSV_FILE)
            print(f"Loaded {len(todo.tasks)} tasks from {CSV_FILE}.")
        elif choice == "7":
            # ذخیره نهایی قبل از خروج
            todo.save_to_csv(CSV_FILE)
            print("Saved. Exiting.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
