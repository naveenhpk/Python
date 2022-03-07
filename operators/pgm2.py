class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def __add__(self,other):
        self.sum=self.mark+other.mark
        return self.sum
    def __mul__(self,other):
        self.pro=self.mark*other.mark
        return self.pro
    def __sub__(self,other):
        self.dif=self.mark-other.mark
        return self.dif
    def __truediv__(self,other):
        self.di=self.mark/other.mark
        return int(self.di)
    def __gt__(self,other):
        if self.mark>other.mark:
            return self.mark
        else:
            return other.mark
    def __lt__(self,other):
        if self.mark<other.mark:
            return other.mark
        else:
            return self.mark
    def __str__(self):
        return self.name
obj1=Student("adarsh",67)
obj2=Student("naveen",66)
print("Addition",obj1+obj2)
print("Multiplication",obj1*obj2)
print("Substraction",obj1-obj2)
print("Division",obj1/obj2)
print("Greatest",obj1>obj2)
print("Lowest",obj1<obj2)
