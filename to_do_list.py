tasks = []

while True:
    print("\n📝 Welcome to To-Do List App!")
    print("1. View Tasks")
    print("2. Add task")
    print("3. Exit")
    print("-" * 20)

    choice = input("Choose (1-3): ")

    if choice == "1":
        if not tasks:
            print("No tasks yet!")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
                print("Total tasks:", len(tasks))

    elif choice == "2":
        task = input("Enter task: ")
        if task.strip() == "":
         print("⚠️ Task cannot be empty!")
        else:
            tasks.append(task)
            print("✅ Thanks! Your task was saved.")
    elif choice == "3":
        print(f"Goodbye 👋 You completed {len(tasks)} tasks today!")

        break
    else:
        print("Invalid choice!")