# Nested Loop is a loop inside another loop. The inner loop will be executed one time for each iteration of the outer loop. Ex:

for i in range(1, 6): # outer loop
    for j in range(1, i+1): # inner loop
        print(i, end=" ")
    print()