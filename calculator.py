while True:

    print("1 Add")
    print("2 Subtract")
    print("3 Multiplication")
    print("4 Division")
    print("Enter Q or q to Exit")


    choice = input("Enter your choice")

    if choice == "q" or choice == "Q":
        break

    number1 = float(input( " Enter the first number : "))
    number2 = float(input("Enter the second number : "))

    if choice == "1":
        print(number1, "+", number2, "=", (number1 + number2))

    elif choice == "2":
        print(number1, "-", number2, "=", (number1 - number2))

    elif choice == "3":
        print(number1, "*", number2, "=", (number1 * number2))

    elif choice == "4":
        if number2==0.0:
            print("Divide by 0 Error")
        else:
            print(number1, "/", number2, "=", (number1 / number2))


    else:
        print("Invalis choice")      

    print()      
