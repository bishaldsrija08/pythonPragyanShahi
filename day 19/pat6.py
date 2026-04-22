"""
   *
  * *
 * * *
* * * *
"""

lines = 4
for i in range(1, lines+1): # outer loop
    # print space
    for j in range(lines, i, -1): # inner loop``
        print(" ", end="")
    
    # print star
    for k in range(1, i+1, 1): # inner loop
        print("* ", end="")
    print()