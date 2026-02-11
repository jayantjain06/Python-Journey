import json
expenses = []
try:
    with open("expenses.json","r") as f:
        expenses = json.load(f)
except FileNotFoundError:
    expenses = []
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
        with open("expenses.json", "w") as f:
            json.dump(expenses, f,indent=4)
        

    elif choice == "2":
        for expense in expenses:
            print(expense["category"], "-", expense["amount"])

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print("Total Spent: ", total)

    elif choice == "4":
        break
