class Computer:
    def __init__(self):
        self.name=input("enter the name") 
        self.prize=int(input("enter the prize"))
        print("Name=",self.name)
        print("prize=",self.prize)
    def update(self):
        self.name=input("enter the name")
        self.prize=int(input("enter the prize"))
        print("Name=",self.name)
        print("prize=",self.prize)
obj=Computer()
obj.update()