# WAP to calculate the sum of digits of a number.

"""
1234 = 1 + 2 + 3 + 4 = 10
"""

num = int(input("Enter a number: "))
sum = 0

while num >0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print("The sum of digits is: ", sum)