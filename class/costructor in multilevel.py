class A:
    def __init__(self):
        print("constructor from a is called")

    def fun1(self):
        print("function 1 is called")
class B(A):
    def __init__(self,name):  #name passing in contructor
        super().__init__()
        self.name=name   
        print("constructor from b is called",self.name)
    def fun2(self):
        print("Funcion 2 is called")
class C(B): 
    def __init__(self,name):  #name passing in contructor  
        print("constructor from c is called")
        super().__init__(name)
        self.name=name 
    def fun3(self):
        print("Funcion 3 is called")
obj=C("naveen")
obj.fun3()

