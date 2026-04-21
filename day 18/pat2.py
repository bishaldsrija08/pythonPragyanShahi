"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

lines = 5
for i in range(1, lines+1): # outer loop
    for j in range (1, i+1): # inner loop
        print(j, end= " ")
    print() # to move to the next line after each iteration of the outer loop


"""
i           j           print(j, end= " ")              print()
1           1           1
2           1 2         1 2
3           1 2 3       1 2 3
4           1 2 3 4     1 2 3 4
5           1 2 3 4 5   1 2 3 4 5
"""