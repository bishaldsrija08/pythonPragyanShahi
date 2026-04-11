# Write a program in Python language to input a number and check whether the number is fully divisible by 5 or not.
num = int(input("Enter a number: "))
if num % 5 == 0:
    print(num, "is fully divisible by 5.")
else:
    print(num, "is not fully divisible by 5.")