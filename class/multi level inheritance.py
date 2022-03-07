class A:
    def fun1(self):
        print("function 1 is called")
class B(A):
    def fun2(self):
        print("Funcion 2 is called")
class C(B):
    def fun3(self):
        print("Funcion 3 is called")
obj=C()
obj.fun3()
obj.fun2()
obj.fun1()
