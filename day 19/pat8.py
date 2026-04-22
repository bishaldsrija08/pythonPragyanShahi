"""
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
"""


lines = 5
for i in range(1, lines+1): # outer loop
    # print space
    for j in range(lines, i, -1): # inner loop``
        print(" ", end="")
    
    # print star
    for k in range(1, i+1, 1): # inner loop
        print(k, end=" ")
    print()