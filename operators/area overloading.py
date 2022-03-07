class Shape:
    def area(self,a=0,b=0):
        if(a!=0 and b!=0):
            self.rec=a*b
            print("Area of rectangle",self.rec)
        else:
            self.squ=a**2
            print("Area of square",self.squ)
obj1=Shape()
obj1.area(4,3)
obj2=Shape()
obj2.area(4)
