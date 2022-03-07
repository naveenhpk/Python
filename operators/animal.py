from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Bird(Animal):
    def speak(self):3
        print("Bird can chirp")
    def move(self):
        print("Bird can move")
class Human(Animal):
    def speak(self):
        print("Human can talk ")
class Snake(Animal):
    def speak(self):
        print("Snake can hiss")
class Tiger(Animal):
    def speak(self):
        print("Tiger can roar")
class Dog(Animal):
    def speak(self):
        print("Dog can Barkkk")
obj1=Bird()
obj1.speak()
obj1.move()
obj2=Human()
obj2.speak()
obj3=Tiger()
obj3.speak()
obj4=Dog()
obj4.speak()
obj5=Snake()
obj5.speak()