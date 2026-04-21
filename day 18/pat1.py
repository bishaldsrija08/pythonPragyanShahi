"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5 5
"""
# To print lines we use outer loop and to print numbers we use inner loop. The inner loop will be executed one time for each iteration of the outer loop. Ex:

lines = 5
for i in range(1, lines+1): # outer loop
    for j in range(1, i+1): # inner loop
        print(i, end= " ")
    print() # to move to the next line after each iteration of the outer loop


"""
i           j           print(i, end= " ")              print()
1           1           1
2           1 2         2 2
3           1 2 3       3 3 3
4           1 2 3 4     4 4 4 4
5           1 2 3 4 5   5 5 5 5 5
"""