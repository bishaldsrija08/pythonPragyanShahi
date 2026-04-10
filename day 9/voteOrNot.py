# WAP wheter a person is eligible to vote or not. (considering the age limit for voting is 18 years)

age = int(input("Enter your age: "))
if age >= 18 and age <= 100:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")