num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))

choice = input("Enter operation (+, -, *, /): ")

if choice == "+":
    sum = num1 + num2
    print("The sum of", num1, "and", num2, "is", sum)
elif choice == "-":
    difference = num1 - num2
    print("The difference of", num1, "and", num2, "is", difference)
elif choice == "*":
    product = num1 * num2
    print("The product of", num1, "and", num2, "is", product)
elif choice == "/":
    if num2 !=0:
        quotient = num1 / num2 #9/0 will give error
        print("The quotient of", num1, "and", num2, "is", quotient)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose from +, -, *, or /.")