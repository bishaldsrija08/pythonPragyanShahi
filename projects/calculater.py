# Make a simple calculator that can add, subtract, multiply, and divide.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

add= num1 + num2
subtract= num1 - num2
multiply= num1 * num2
divide= num1 / num2

print("The sum of", num1, "and", num2, "is", add)
print("The difference of", num1, "and", num2, "is", subtract)
print("The product of", num1, "and", num2, "is", multiply)
print("The quotient of", num1, "and", num2, "is", divide)

# operation = input("Enter operation (+, -, *, /): ")

# if operation == "+":
#     result = num1 + num2
#     print("The sum of", num1, "and", num2, "is", result)
# elif operation == "-":
#     result = num1 - num2
#     print("The difference of", num1, "and", num2, "is", result)
# elif operation == "*":
#     result = num1 * num2
#     print("The product of", num1, "and", num2, "is", result)
# elif operation == "/":
#     if num2 != 0:
#         result = num1 / num2
#         print("The quotient of", num1, "and", num2, "is", result)
#     else:
#         print("Error: Division by zero is not allowed.")