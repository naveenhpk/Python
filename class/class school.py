class School:
    schoolname="ghss"  #class variable wiill be same in every object
    place="payyanur"
    phone=54545
    
    def add(self):
        self.schoolname=input("enter the school name")
        self.place=input("Enter the place")
        self.phone=int(input("enter the phone number"))
    def display(self):
        print("School name:",self.schoolname)
        print("School location:",self.place)
        print("phone number",self.phone)

obj=School()
obj.add()
obj.display()


obj2=School()
obj2.add()
obj2.display()
