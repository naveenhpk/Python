class A:
    def show(self):
        print("A I ")
class B(A):
    def show(self):
        print("B IS") # b overides A
obj=B()
obj.show()