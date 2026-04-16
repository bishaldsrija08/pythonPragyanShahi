# Given a number, write a program to count the number of digits in it using a loop.

"""
n= 45453 => 5 digits
"""

n = int(input("Enter a number: ")) #12
count = 0
while n>0:
    n =int(n/10) # n=n//10
    count = count + 1
print("Number of digits: ", count)