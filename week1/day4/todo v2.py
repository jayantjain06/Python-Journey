tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark done")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice =="1":
        task = input("Enter Task: ")
        tasks.append([task, False])

    elif choice =="2":
        for i, (t, done) in enumerate(tasks):
            status = "✓" if done else " "
            print(f"{i+1}. [{status}] {t}")


    elif choice == "3":
        delete = int(input("delete task number: "))
        tasks.pop(delete-1)
        
    elif choice == "4":
        num = int(input("Task number: "))
        if 0 < num <= len(tasks):
            tasks[num-1][1] = True
        else:
            print("Invalid number")


    elif choice =="5":
        break