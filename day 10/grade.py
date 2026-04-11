# WAP to check grade of a student based on marks obtained in a subject. The grading system is as follows:
# Marks >= 90 and <= 100: Grade A
# Marks >= 80 and < 90: Grade B
# Marks >= 70 and < 80: Grade C
# Marks >= 60 and < 70: Grade D
# Marks < 60: Grade F

marks = float(input("Enter the marks obtained in the subject: "))

if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=80 and marks<90:
    print("Grade B")
elif marks>=70 and marks<80:
    print("Grade C")
elif marks>=60 and marks<70:
    print("Grade D")
elif marks<60:
    print("Grade F")
else:
    print("Invalid marks entered. Please enter marks between 0 and 100.")