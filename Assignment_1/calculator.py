def calculator():
    while True:
        operation = input("Enter an operation (+, -, *, /): ")

        if operation not in ("+", "-", "*", "/"):
            print("please choose values from the given list.")
            continue

        try :

            num1 = float(input("Enter the first number:"))
            num2 = float(input("Enter the second number:"))
        except ValueError:
            print("please enter numeric values")
            continue
        
        if operation == "+":
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result}")
        elif operation == "/":
           
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is {result}")
            else:
                print("dont enter 0 for num2")
        else:
            print("Error: Invalid operation.")

        if input("Do you want to perform another calculation? (yes/no): ") != "yes":
           print("Thanks for using my calculator!")
           break


calculator()

