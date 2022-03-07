class Average:
    def average(self,p=0,m=0,c=0):
        if(m!=0 and p!=0 and c!=0):
            self.avg=(p+c+m)/3
            print("Average =",self.avg)
        elif(m!=0 and p!=0):
            self.avg=(p+m)/2
            print("Average =",self.avg)
        else:
            self.avg=p
            print("Average =",self.avg)
obj=Average()
obj.average(30,10,45)
print("____________________________")
obj2=Average()
obj2.average(30,45)
print("____________________________")

obj3=Average()
obj3.average(30)
print("____________________________")
