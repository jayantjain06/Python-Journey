def get_numbers():
    a = float(input("Enter your first number:  "))
    b = float(input("Enter your second number:  "))
    return a, b
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        print("cannot divide by zero")
    return a/b
while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice:  ")

    if choice == "1":
        a, b = get_numbers()
        print(f"Result: {add(a,b)}")

    elif choice == "2":
        a, b = get_numbers()
        print(f"Result: {subtract(a,b)}")

    elif choice == "3":
        a, b = get_numbers()
        print(f"Result: {multiply(a,b)}")  

    elif choice == "4":
        a, b = get_numbers()
        
        print(f"Result: {divide(a,b)}")      

    elif choice == "5":
        break
    
    else:
        print("Invalid Input") 
