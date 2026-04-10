# WAP to check whether a person can get citizenship or not. (considering the age limit for citizenship is 16 years)

age = int(input("Enter your age: "))
if age >= 16 and age <=100:
    print("You are eligible for citizenship.")
else:
    print("You are not eligible for citizenship.")