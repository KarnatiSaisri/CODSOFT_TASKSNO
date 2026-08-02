while True:
    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "5":
        print("Thank you!")
        break
    elif choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    if choice == "1":
        print("Result =", num1 + num2)
    elif choice == "2":
        print("Result =", num1 - num2)
    elif choice == "3":
        print("Result =", num1 * num2)
    elif choice == "4":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid choice!")