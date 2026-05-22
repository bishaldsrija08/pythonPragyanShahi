class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self): # getter method to access the private attribute __age
        return self.__age

p1 = Person("Alice", 30)
print(p1.name)  # Output: Alice
print(p1.__age)  # This will raise an AttributeError because __age is private
print(p1.get_age())   # Output: 30