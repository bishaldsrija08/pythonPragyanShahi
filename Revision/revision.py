# Recursion
"""
When a function calls itself, it is called recursion. A recursive function is a function that calls itself in order to solve a problem. The function typically has a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.
"""

# 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 3628800

# Fibonacci Sequence CW


# Lambda Function
"""
Lambda functions are anonymous functions that can have any number of arguments but only one expression. They are often used for short, simple functions that are not reused elsewhere in the code. The syntax for a lambda function is: lambda arguments: expression.
"""

abc = lambda x: x * 2  # This is a lambda function that takes one argument x and returns x multiplied by 2
print(abc(5))  # Output: 10

name = lambda first, last: f"{first} {last}"  # This is a lambda function that takes two arguments, first and last, and returns a formatted string with the full name
print(name("John", "Doe"))  # Output: John Doe

# Cw: Write a lambda function that takes two numbers as input and returns their sum.



# JSON

# CW: Write a Python program that uses the json module to convert a Python dictionary into a JSON string and then back into a dictionary.