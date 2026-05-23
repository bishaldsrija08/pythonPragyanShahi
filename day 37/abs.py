from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def greet(self):
        pass

class EnglishGreet(Greet):
    def greet(self):
        return "Hello!"
    
# g = EnglishGreet()
# print(g.greet())

g = Greet()  # This will raise an error because Greet is an abstract class and cannot be instantiated.