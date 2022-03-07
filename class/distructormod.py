class School:
    def __init__(self,a,b):     #constructor
        self.a=a 
        self.b=b
        print("Hello i am from constructor ",self.a,"%",self.b)
    def display(self):
        self.c=self.a+self.b
        return self.c
    def __del__(self):   #distructor 
        print(self," is deleted")

obj=School(6,7)
del obj   #manually deleting an object
obj2=School(5,8) #in this distructor automaticlly calls
print("hi")
print("hi")
print("hi")