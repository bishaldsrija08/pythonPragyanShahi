# Break is a statement that allows you to exit a loop prematurely. When the break statement is executed, the loop is immediately terminated, and the program continues with the next statement after the loop.

for i in range(1, 11, 1):
    if i == 9:
        break
    print(i)