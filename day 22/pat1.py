"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
lines = 5
for i in range(1, lines+1, 1):
    for j in range(1, i+1, 1):
        print(j, end=" ")
    print()
    
# Dry run

"""
i                       j                       print(j, end=" ")       print()
1                       1                           1                       \n
2                       1 2                         1 2                     \n
3                       1 2 3                       1 2 3                   \n
4                       1 2 3 4                     1 2 3 4                 \n
5                       1 2 3 4 5                   1 2 3 4 5               \n
"""