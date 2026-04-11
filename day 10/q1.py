# Write a program in Python language that inputs any number and checks number is divisible by 6 but not 13.

num = int(input("Enter a number: "))

if num % 6 ==0 and num %13 !=0:
    print(num, "is divisible by 6 but not 13.")
else:
    print(num, "is not divisible by 6 or it is divisible by 13.")