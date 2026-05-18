class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    pass

s1 = Student("Alice", 20)
s2 = Student("Bob", 22)
s1.print_info()  # Output: Name: Alice, Age: 20
s2.print_info()  # Output: Name: Bob, Age: 22