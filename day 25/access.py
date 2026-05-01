thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[1]) # Output: banana

print(thislist[-1]) # Output: mango

print(thislist[2:5]) # Output: ['cherry', 'orange', 'kiwi']

print(thislist[:4]) # Output: ['apple', 'banana', 'cherry', 'orange']

print(thislist[2:]) # Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']

print(thislist[-4:-1]) # Output: ['orange', 'kiwi', 'melon']

if "apple" in thislist:
    print("Yes, 'apple' is in the list")