# Funksie om twee getalle by mekaar te tel
def add(x, y):
    return x + y

# Funksie om twee getalle van mekaar af te trek
def subtract(x, y):
    return x - y

# Funksie om twee getalle met mekaar te maal
def multiply(x, y):
    return x * y

# Funksie om twee getalle met mekaar te deel
def divide(x, y):
    if y == 0:
        return "Can't divide by zero"
    return x / y

# Basiese sakrekenaar funksies
def calculator():
    while True:
        print("Select an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Clear")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '6':
            print("Exiting calculator.")
            break
        
        # Maak die lyntjie skoon om byvoorbeeld n nuwe berekening te begin
        if choice == '5':
            print("^" * 100)
            continue

        if choice in ('1', '2', '3', '4'):
            try:
                x = float(input("Enter firts number: "))
                y = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(x, "+", y, "=", add(x, y))
            elif choice == '2':
                print(x, "-", y, "=", subtract(x, y))
            elif choice == '3':
                print(x, "*", y, "=", multiply(x, y))
            elif choice == '4':
                print(x, "/", y, "=", divide(x, y))

        else:
            print("Invalid input")

# Hardloop die sakrekenaar
calculator()
