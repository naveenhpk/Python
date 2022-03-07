class Car:
    model="altroz"
    milege=25
    def __init__(self,color,version):
        self.color=color
        self.version=version
    def display(self):
        print("Car model=",self.model)
        print("milege=",self.milege)
        print("Color=",self.color)
        print("Version=",self.version)
    @classmethod
    def update(self):
        print("Update car")
        self.model=input("Enter the new model")
    @staticmethod    
    def show():
        print("Company name: Tata")
        print("Established since 1982")
obj=Car('black','petrol')
obj.display()
Car.update()
obj.display()
Car.show()

