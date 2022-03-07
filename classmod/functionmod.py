#function define
def myfun(a,b):#using arguments
    print("sum=",a+b)
a=int(input("enter 1st number")) 
b=int(input("enter 2nd number"))
#functiom call using argue ments
myfun(a,b)

# #3 TYPES OF ARGUMENT  REQUIRED,KEYWORD,DEFAULT,VARIABLE LENTH

# #KEYWORD ARGUMENT CALL
def mydet(name,age):
    print("Name is =",name)
    print("Age is ",age)
a=input("enter ur name")
b=int(input("enter ur age"))
mydet(name=a,age=b)

#default argument
def mydet(name,age=21):
    print("Name is =",name)
    print("Age is ",age)
a=input("enter ur name")
b=int(input("enter ur age"))
mydet(a,b)

#variable length argument
def mydet(*name):
    print("Name is =",name[0])
    print("Name is =",name[1])
a=input("enter ur name")
b=int(input("enter ur age"))
mydet(a,b)

#return is used give value outside the function 
