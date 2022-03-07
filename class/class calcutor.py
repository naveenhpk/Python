class Calculator:
    def operations(self):
        self.a=int(input("Enter the 1st number"))
        self.b=int(input("Enter the 2nd number"))
        self.add=self.a+self.b
        self.diff=self.a-self.b
        self.mul=self.a*self.b
        self.div=self.a/self.b
    def display(self):
        print("Sum=",self.add)
        print("Difference=",self.diff)
        print("Product=",self.mul)
        print("Difference=",self.div)
obj=Calculator()
obj.operations()
obj.display()


