"""
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""
lines = 5
for i in range(lines, 0, -1):
    for j in range(1, i+1, 1):
        print(i, end = " ")
    print()

    """
    i       j                   print(i, end = " ")
    5       1 2 3 4 5           5 5 5 5 5
    4       1 2 3 4             4 4 4 4
    3       1 2 3               3 3 3
    2       1 2                 2 2
    1       1                    1 
    """