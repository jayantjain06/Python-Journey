expenses = []
total=0
while True:
    print("\n1. Add expense")
    print("2. View all expense")
    print("3. Show total spent")
    print("4. Exit")
    choice=input("Choose what you wanna do: ")
    if choice == "1":
        
        amount=int(input("Amount: "))
        category=input("Category: ")
        expenses.append({
            "amount":amount,
            "category":category
        })
        total = sum(exp["amount"] for exp in expenses)

    elif choice == "2":
        for exp in expenses:
            print(exp["category"], "-", exp["amount"])

    elif choice == "3":
        print("Total Spent: ", total)

    elif choice == "4":
        break
