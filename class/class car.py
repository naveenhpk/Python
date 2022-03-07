class Car:
    cmpyname="suzuki"
    model="swift"
    milege=24
    
    def add(self):
        self.cmpyname=input("enter the company name")
        self.model=input("Enter the model")
        self.milege=int(input("enter the milege"))
    def display(self):
        print("Car name:",self.cmpyname)
        print("Car location:",self.model)
        print("phone number",self.milege)

obj=Car()
obj.add()
obj.display()

obj3=Car()
obj3.add()
obj3.display()

obj2=Car()
obj2.add()
obj2.display()