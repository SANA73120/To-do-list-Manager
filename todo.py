import json
from datetime import datetime, timedelta

# File where tasks will be saved (you can change the path if needed)
TASKS_FILE = "C:/Users/Sana Khan/Desktop/week1python/tasks.json"

# ---------------- LOAD AND SAVE ----------------

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except:
        return []  # Return empty list if no file yet

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# ---------------- TASK FUNCTIONS ----------------

# Add a new task
def add_task(tasks):
    description = input("⎚ Enter task description: ")
    due_date = input("⎚ Enter due date (YYYY-MM-DD) or leave blank: ")
    priority = input("⎚ Enter priority (Low/Medium/High): ").capitalize()

    if priority not in ["Low", "Medium", "High"]:
        priority = "Low"  # Default priority

    task = {
        "description": description,
        "due_date": due_date if due_date else None,
        "status": "Pending",
        "priority": priority
    }
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!")

# Show all tasks
def view_tasks(tasks):
    if not tasks:
        print("📂 No tasks found.")
        return

    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, 1):
        reminder = ""
        if task["due_date"]:  # Check if task has a due date
            due = datetime.strptime(task["due_date"], "%Y-%m-%d")
            if due <= datetime.now() + timedelta(days=3) and task["status"] == "Pending":
                reminder = "⚠️ Due Soon!"

        print(f"{i}. {task['description']} | Due: {task['due_date']} | "
              f"Priority: {task['priority']} | Status: {task['status']} {reminder}")

# Mark a task as completed
def mark_complete(tasks):
    view_tasks(tasks)
    num = int(input("☁︎ Enter task number to mark complete: ")) - 1
    if 0 <= num < len(tasks):
        tasks[num]["status"] = "Completed"
        save_tasks(tasks)
        print("✅ Task completed!")
    else:
        print("⚠ Invalid number.")

# Edit a task
def edit_task(tasks):
    view_tasks(tasks)
    num = int(input("⎚ Enter task number to edit: ")) - 1
    if 0 <= num < len(tasks):
        new_desc = input("✿ New description (leave blank to keep): ")
        new_due = input("✿ New due date (YYYY-MM-DD) or leave blank: ")
        new_priority = input("✿ New priority (Low/Medium/High) or leave blank: ").capitalize()

        if new_desc:
            tasks[num]["description"] = new_desc
        if new_due:
            tasks[num]["due_date"] = new_due
        if new_priority in ["Low", "Medium", "High"]:
            tasks[num]["priority"] = new_priority

        save_tasks(tasks)
        print("✏️ Task updated!")
    else:
        print("⚠ Invalid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    num = int(input("⎚ Enter task number to delete: ")) - 1
    if 0 <= num < len(tasks):
        tasks.pop(num)
        save_tasks(tasks)
        print("🗑 Task deleted!")
    else:
        print("⚠ Invalid number.")

# ---------------- REMINDERS ----------------

# Show reminders when program starts
def show_reminders(tasks):
    print("\n🔔 Checking for tasks due soon...")
    for task in tasks:
        if task["status"] == "Pending" and task["due_date"]:
            due = datetime.strptime(task["due_date"], "%Y-%m-%d")
            if due <= datetime.now() + timedelta(days=3):
                print(f"⚠️ Reminder: {task['description']} (Due: {task['due_date']})")

# ---------------- MAIN MENU ----------------

def main():
    tasks = load_tasks()
    show_reminders(tasks)  # Show reminders first

    while True:
        print("\n=====✩✩✩ TO-DO LIST MANAGER ✩✩✩=====")
        print("1. Add Task +++")
        print("2. View Tasks >>>")
        print("3. Mark Task as Completed ✅✅✅")
        print("4. Edit Task ✏️✏️✏️")
        print("5. Delete Task ☾☾☾")
        print("6. Exit ✩✩✩")

        choice = input("♡ Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid choice!")

# Run the program
if __name__ == "__main__":
    main()
