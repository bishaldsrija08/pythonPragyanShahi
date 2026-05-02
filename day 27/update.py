x = ("apple", "banana", "cherry")
y = list(x)
# print(y)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Convert a string to a tuple
name = "John Doe"
tuple_name = tuple(name)
print(tuple_name)