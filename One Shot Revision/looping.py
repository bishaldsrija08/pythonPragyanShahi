"""
looping is the process of repeating a block of code until a certain condition is met. In Python, there are two main types of loops: for loops and while loops.
initial value, final value, increment/decrement
"""


# for loop => for variable in iterable:
# while loop => while condition: while loops are used when the number of iterations is not known beforehand, while for loops are used when the number of iterations is known or can be determined from the iterable.

# for loop example
for i in range(1, 11, 1):
    print(i)

# while loop example
i = 1
while i <= 10:
    print(i)
    i += 1