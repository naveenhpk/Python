class Vehicle:
    vehicle_brand="Honda"
    def __init__(self):  #instance metod
        print("Constructor is called")
    

    def display(self,name):
        self.name=name
        print("Vehicle is a",self.name,"Brand is",self.vehicle_brand)

    @classmethod       #class metod
    def Get(cls):
        print(cls.vehicle_brand)
    
    @staticmethod     #static metod
    def show():
        print("program is done")
    
obj=Vehicle()   #instance metod access
obj.display("Activa")


Vehicle.Get()  #class metod accessing

Vehicle.show()