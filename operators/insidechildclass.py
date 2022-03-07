class Base:
    def display(self):
        print("Inside base class")
class Derived(Base):
    def show(self):
        Base.display(self)
        print("Inside derived class")
obj=Derived()
obj.show()