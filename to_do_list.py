tasks = []

while True:
    print("\nTo-Do List")
    print("1. View Tasks")
    print("2. Add tassk")
    print("3. Exit")

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
        tasks.append(task)
        print("Task added!")
    elif choice == "3":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice!")