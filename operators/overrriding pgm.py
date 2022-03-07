class Parent:
    def details(self):
        print("****Parent details****")
        self.name=input("Enter the name ")
        self.age=int(input("Enter the age"))
        self.phn=int(input("Enter the phone number"))
        print("Name:",self.name)
        print("Age:",self.age)
        print("Phone number",self.phn)

class Child(Parent):
    def details(self):
        print("****Child details***")
        self.name=input("Enter the name ")
        self.mark=int(input("Enter the mark"))
        print("Name:",self.name)
        print("Mark:",self.mark)
obj=Child()
obj.details()
