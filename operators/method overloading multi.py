class Multiplication:
    def multiplcation(self,p=None,m=None,c=None,d=None):
        if(m!=None and p!=None and c!=None and d!=None):
            self.pro=(p*c*m*d)
            print("Product =",self.pro)
        elif(m!=None and p!=None and c!=None):
            self.pro=(p*c*m)
            print("Product =",self.pro)
        elif(m!=None and p!=None):
            self.pro=(p*m)
            print("Product =",self.pro)
        else:
            self.pro=p
            print("Producut =",self.pro)
obj=Multiplication()
obj.multiplcation(30,10,45,15)
print("____________________________")
obj1=Multiplication()
obj1.multiplcation(30,10,45)
print("____________________________")
obj2=Multiplication()
obj2.multiplcation(30,45)
print("____________________________")

obj3=Multiplication()
obj3.multiplcation(30)
print("____________________________")
