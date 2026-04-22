"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

lines = 5
for i in range(1, lines+1): # outer loop
    for j in range(1, i+1, 1): # inner loop
        print(j, end=" ")
    print()