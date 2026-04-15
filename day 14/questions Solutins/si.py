# Write a program in python language to take principal, rate, and time and calculate the simple interest. [hint: SI=(P*R*T)/100]

P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time in years: "))

SI = (P * R * T) / 100
print("The simple interest is:", SI)