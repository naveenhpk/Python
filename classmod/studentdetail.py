data={}
def add():
    i=int(input("ID :"))
    name=input("NAME :")
    age=int(input("AGE :"))
    place=input("PLACE :")
    details={}
    details['name']=name
    details['age']=age
    details['place']=place
    data[i]=details
    print(data)
def display():
    a=int(input("enter id"))
    if a not in data.keys():
        print("id not identified")
    else:
        print(data[a])
def update():
    i=int(input("enter modifying id"))
    if i not in data.keys():
        print("id not identified")
    else:
        print("enter the modifications.")
        x=input("NAME :")
        data[i]['name']=x
        y=input("AGE :")
        data[i]['age']=y  
        z=input("PLACE :")
        data[i]['place']=z       
def delete():
    i=int(input("enter id to delete"))
    data.pop(i)
def operations():
    print("-----------Student details---------")
    print("1.Add a student")
    print("2.Display  student details")
    print("3.Update student details")
    print("4.Delete a student")
    print("5.Exit")
    n=int(input("ENTER CHOICE :"))
    if n>5:
        print("ENTER VALID CHOICE")
    elif n==1:
        add()
    elif n==2:
        display()
    elif n==3:
        update()
    elif n==4:
        delete()
    elif n==5:
        print("..EXIT..")
        exit()
    else:
        print("Invalid selection")
        print("")
    operations()        
operations()





