# Mini Project: To-Do List with File Storage

FILENAME = "tasks.txt"

def add_task(task):
    with open(FILENAME, "a") as f:
        f.write(task + "\n")
    print("Task added.")

def view_tasks():
    try:
        with open(FILENAME, "r") as f:
            tasks = f.readlines()
            if not tasks:
                print("No tasks found.")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No task file found.")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
