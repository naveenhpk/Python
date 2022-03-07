class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __str__(self):
        return str(self.real)+' + '+str(self.img)+'i'
    def __add__(self,other):
        print("Addition of complex number")
        r = self.real + other.real
        i = self.img + other.img
        return Complex(r,i)
    def __sub__(self,other):
        print("Substraction of complex number")
        r = self.real - other.real
        i = self.img - other.img
        return Complex(r,i)
    def __mul__(self,other):
        print("Multiplication of complex number")
        r =self.real*other.real-self.img*other.img
        i =self.real*other.img+self.img*other.real
        return Complex(r,i)
    # def __str__(self):
    #     return str(self.real)+' + '+str(self.img)+'i'
real=int(input("Enter real part of first number"))
img=int(input("Enter imaginary part of first number"))
x=int(input("Enter real part of second number"))
y=int(input("Enter imaginary part of second number"))
obj1=Complex(real,img)
print(obj1)
obj2=Complex(x,y)
print(obj2)
print(obj1+obj2)
print(obj1-obj2)
print(obj1*obj2)