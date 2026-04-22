""""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

lines = 5
for i in range(lines, 0, -1):
    for j in range(lines, lines - i, -1):
        print(j, end=" ")
    print()
    
"""
i               j                   print(j, end=" ")
5               5 4 3 2 1           5 4 3 2 1
4               5 4 3 2             5 4 3 2
3               5 4 3               5 4 3
2               5 4                 5 4
1               5                   5
"""