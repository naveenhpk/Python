class School:
    schoolname="ghss"  #class variable wiill be same in every object
    place="payyanur"
    phone=54545
    

obj=School()
print(obj.schoolname)
School.schoolname="alphonsa"   #class variable changing   to evry object of same class
#class.classs varaiable name=changing value
obj2=School()
print(obj.schoolname)

obj=School()
print(obj.schoolname)