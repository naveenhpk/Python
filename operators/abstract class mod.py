from abc import ABC,abstractmethod
class Human(ABC):
    @abstractmethod
    def see(self):
        pass

class Men(Human):
    def see(self):   #for an absytract clas the the inhr=eited class need all the methods in abstract class from the parent class
        print("men can walk")

obj=Men()
obj.see()