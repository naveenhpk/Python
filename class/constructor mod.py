class School:
    def __init__(self,a,b):
        self.a=a 
        self.b=b
        print("Hello i am from constructor ",self.a,"%",self.b)
    def display(self):
        self.c=self.a+self.b
        return self.c
obj=School(6,7)
print(obj.display())