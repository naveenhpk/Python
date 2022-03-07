class Student():
    school="KV"
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    def display(self):
        print("ID",self.id)
        print("Name:",self.name)
        print("Age :",self.age)
obj1=Student(1,"sara",10)
obj1.display()
obj2=Student(2,"Jose",20)
obj2.display()

print("_______")
print("ID:",getattr(obj1,"id"))
print("NAME",getattr(obj1,"name"))
print("AGE",getattr(obj1,"age"))
print("*******************")
print("Updating ID 2")
setattr(obj2,"name","Krish")
obj2.display()
print("*******")
print("Checking place in the data:",hasattr(obj1,"place"))
setattr(obj1,"place","Kannur")
print("Place",obj1.place)