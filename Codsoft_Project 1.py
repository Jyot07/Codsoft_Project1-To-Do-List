
# Simple To-Do List App
# Just a small command-line program to add, view, complete, and delete tasks.

todo_list = []

def show_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.\n")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(todo_list, start=1):
            status = "[x]" if task["done"] else "[ ]"
            print(f"{i}. {status} {task['title']}")
    print()

def add_task():
    task_name = input("Enter a new task: ").strip()
    if task_name:
        todo_list.append({"title": task_name, "done": False})
        print(f"Task added: {task_name}\n")
    else:
        print("Task name can't be empty.\n")

def complete_task():
    show_tasks()
    if todo_list:
        try:
            num = int(input("Which task number did you finish? "))
            if 1 <= num <= len(todo_list):
                todo_list[num - 1]["done"] = True
                print(f"Marked task {num} as done.\n")
            else:
                print("That number is not in the list.\n")
        except ValueError:
            print("Please enter a valid number.\n")

def delete_task():
    show_tasks()
    if todo_list:
        try:
            num = int(input("Which task number do you want to delete? "))
            if 1 <= num <= len(todo_list):
                removed = todo_list.pop(num - 1)
                print(f"Deleted: {removed['title']}\n")
            else:
                print("That number is not in the list.\n")
        except ValueError:
            print("Please enter a valid number.\n")

def main():
    print("Welcome to the To-Do List App")
    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye! Stay organized.")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run the app
main()
