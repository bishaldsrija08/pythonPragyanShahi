# Make a calulator using if, and looops

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")

while True:
    if operation == "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
        break
    elif operation == "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
        break
    elif operation == "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
        break
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
            break
        else:
            print("Error: Division by zero is not allowed.")
            break
    else:
        print("Invalid operation. Please enter a valid operation (+, -, *, /).")
        operation = input("Enter the operation again (+, -, *, /): ")