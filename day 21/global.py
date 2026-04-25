a = 10
def square(x):
    global a
    a = a + 1
    print(a)
    return x * x

print(square(5))