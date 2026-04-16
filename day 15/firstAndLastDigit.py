# Given a number, write a program to find the first and last digits of it.
# n = 24234234 = first digit = 2, last digit = 4

n = int(input("Enter a number: ")) #9123

last_digit = n % 10
print("Last digit: ", last_digit)

while n>=10:
    n= n//10
print("First digit: ", n)