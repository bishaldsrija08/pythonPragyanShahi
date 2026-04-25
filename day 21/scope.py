
def add():
    global a
    a = 5
    # global keyword is used to declare that a variable inside a function is global (outside the function). It allows you to modify the variable outside of the function.
    print(a)

add()
a = a + 5
print(a) # This will raise an error because 'a' is not defined in the global scope.