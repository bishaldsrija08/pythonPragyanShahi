thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# thislist[0]= "watermelon"
print(thislist)


# thislist[1:3] = ["watermelon", "grape"]

thislist.insert(2, "watermelon")
print(thislist)

idx = thislist.index("banana")
print(idx) # Output: 1

thislist[idx] = "grape"
print(thislist)