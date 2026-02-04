tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice =="1":
        task = input("Enter Task: ")
        tasks.append(task)

    elif choice =="2":
        for i,t in enumerate(tasks):
            print(i+1,t)

    elif choice == "3":
        delete = int(input("delete task number: "))
        tasks.pop(delete-1)
        
    elif choice =="4":
        break