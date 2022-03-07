class A:
    def fun1(self):
        print("function 1 is called")

    def same(self):
        print("a is called")
class B():
    def fun2(self):
        print("Funcion 2 is called")

    def same(self):
        print("b is called")

class C(B , A):
    def fun3(self):
        self.fun1()
        self.fun2()
        self.same()  #resolution chechking funcn with same name in 2 different class
        print("Function 3 is called")

obj=C()
obj.fun3()

