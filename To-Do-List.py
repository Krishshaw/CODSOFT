def display_todo_list(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list):
            print(f"{i + 1}. {task}")

def add_task(todo_list):
    task = input("\nEnter the new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added.")

def remove_task(todo_list):
    display_todo_list(todo_list)
    if todo_list:
        task_num = int(input("\nEnter the task number to remove: "))
        if 0 < task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Task '{removed}' removed.")
        else:
            print("Invalid task number.")

def update_task(todo_list):
    display_todo_list(todo_list)
    if todo_list:
        task_num = int(input("\nEnter the task number to update: "))
        if 0 < task_num <= len(todo_list):
            new_task = input("Enter the new task: ")
            todo_list[task_num - 1] = new_task
            print(f"Task {task_num} updated.")
        else:
            print("Invalid task number.")

def clear_tasks(todo_list):
    todo_list.clear()
    print("\nAll tasks cleared.")

def todo_list_app():
    todo_list = []

    while True:
        print("\n1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Update Task")
        print("5. Clear All Tasks")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            update_task(todo_list)
        elif choice == '5':
            clear_tasks(todo_list)
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")

todo_list_app()