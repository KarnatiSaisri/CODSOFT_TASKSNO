tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Complete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter a task: ")

        task_data = {
            "name": task,
            "completed": False
        }

        tasks.append(task_data)
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks yet.")

        else:
            for i, task in enumerate(tasks):

                if task["completed"]:
                    print(i + 1, ".", task["name"], "- Completed")
                else:
                    print(i + 1, ".", task["name"], "- Pending")

    # Delete Task
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to delete.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks):
                print(i + 1, ".", task["name"])

            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                deleted = tasks.pop(number - 1)
                print("Deleted:", deleted["name"])
            else:
                print("Invalid task number.")

    # Complete Task
    elif choice == "4":

        if len(tasks) == 0:
            print("No tasks yet.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks):
                print(i + 1, ".", task["name"])

            number = int(input("Enter task number to complete: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["completed"] = True
                print("Task completed!")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "5":
        print("Goodbye!")
        break

    # Invalid choice
    else:
        print("Invalid choice.")
