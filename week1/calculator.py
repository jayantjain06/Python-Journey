while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice:  ")

    if choice == "1":
        a = float(input("Enter your first number:  "))
        b = float(input("Enter your second number:  "))
        print(f"{a} + {b} = {a+b}")

    elif choice == "2":
        a = float(input("Enter your first number:  "))
        b = float(input("Enter your second number:  "))
        print(f"{a} - {b} = {a-b}")

    elif choice == "3":
        a = float(input("Enter your first number:  "))
        b = float(input("Enter your second number:  "))
        print(f"{a} * {b} = {a*b}")  

    elif choice == "4":
        a = float(input("Enter your first number:  "))
        b = float(input("Enter your second number:  "))
        if b==0:
            print("cannot divide by zero")
        print(f"{a} / {b} = {a/b}")      

    elif choice == "5":
        break
    
    else:
        print("Invalid Input") 
