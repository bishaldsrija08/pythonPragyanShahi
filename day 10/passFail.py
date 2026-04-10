# WAP to check wheter a student has passed or failed. (considering the pass mark is 40)

marks = int(input("Enter your marks: "))

if marks>=40 and marks<=100:
    print("Congratulations! You have passed.")
else:
    print("Sorry! You have failed. Better luck next time.")