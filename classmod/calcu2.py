class Calculator:

    def operations(self):
        print("CHOICES")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        self.x=int(input("enter the choice"))
        self.a=int(input("Enter the 1st number"))
        self.b=int(input("Enter the 2nd number"))
        self.add=self.a+self.b
        self.diff=self.a-self.b
        self.mul=self.a*self.b
        self.div=self.a/self.b    
    def display(self):
        if self.x==1:
            print("Sum=",self.add)
        elif self.x==2:
            print("differnce=",self.diff)
        elif self.x==3:
            print("Product=",self.mul)
        elif self.x==4:
            print("Divsion=",self.div)
        else:
            print("invalid")
obj=Calculator()
while True:
    obj.operations()
    obj.display()
    con=input("do you want to continue y.Yes n.No")
    if con=='n':
    	break



