# While loop is used to execute a block of code repeatedly until a certain condition is met.
# The syntax of a while loop is as follows:
# while condition:
#     # code to be executed

# Example of a while loop that prints numbers from 1 to 10

i = 1 # Initialize the variable i to 1
while i<=10: # The loop will continue to execute as long as i is less than or equal to 10
    print(i, end=' ')
    i=i+1 # Increment the value of i by 1 in each iteration to avoid an infinite loop
