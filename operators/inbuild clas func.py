
class Student():
    age=18
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print("id is",self.id)
        print("nameis:",self.name)
class Circle():
    age=18
    def __init__(self,id,name):
        self.id=id
        self.name=name
    
obj=Student(1,"naveen")
obj.display()
setattr(obj,"place","Kozhikode") #settattr(object,key,attribute)
print(hasattr(obj,"place"))
print(getattr(obj,"place"))
print(isinstance(obj,Student))
print(isinstance(obj,Circle))