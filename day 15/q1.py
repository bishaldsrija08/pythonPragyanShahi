# Take a number n as input and print the sum of the first n natural numbers using a loop.

n = int(input("Enter a number: ")) # n=5
sum =0
for i in range(1, n+1, 1):
    sum = sum +i #sum = 1, 3, 6, 10, 15
print("The sum of the first", n, "natural numbers is:", sum)