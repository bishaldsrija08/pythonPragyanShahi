# Write a program in python language to find the square root of a number.

import math

num = float(input("Enter a number: "))
if num < 0:
    print("Cannot compute the square root of a negative number.")
else:
    sqrt = math.sqrt(num)
    print(f"The square root of {num} is {sqrt}.")