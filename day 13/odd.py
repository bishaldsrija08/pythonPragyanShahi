# WAP to print odd numbers from 1 to 100 using continue statement.


for i in range(1, 101, 1):
    if i % 2 ==0:
        continue
    print(i, end=" ")