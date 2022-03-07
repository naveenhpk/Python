data={}
def addmember():
    name=input("NAME :")
    phone=[]
    ph=int(input("Enter  how many numbers  : "))  
    print("enter the numbers")
    for i in range(ph): 
        num=int(input()) 
        phone.append(num)  
    email=[]   
    em=int(input("Enter  how many email : "))  
    print("enter the emails")
    for i in range(em): 
        emid=(input()) 
        email.append(emid)
    data[name]={"Phone":phone,"Email":email}
    print("**Contact saved**")
    print(data)
def dispnumb():
	name=input("Enter the name to search the phone number:")
	if name in data:
	   print(data[name]["Phone"])
	else:
		print("invalid")
def dispemail():
	name=input("Enter the name to search Email:")
	if name in data:
	   print(data[name]["Email"])
	else:
		print("invalid name")
def update():
    name=input("enter modifying name")
    if name not in data:
        print("name not identified")
    else:
        phone=[]
        ph=int(input("Enter  how many numbers  : "))  
        print("enter the numbers")
        for i in range(ph): 
            num=int(input()) 
            phone.append(num)  
        email=[]   
        em=int(input("Enter  how many email : "))  
        print("enter the emails")
        for i in range(em): 
            emid=(input()) 
            email.append(emid)
        data[name]={"Phone":phone,"Email":email}
    print("**Contact Updated**")
def delete():
    name=input("Enter the name to delete")
    if name in data:
        del data[name]
        print("**Contact deleted***")
    else:
        print("invalid name")
def operations():
    print("-----------PHONEBOOK---------")
    print("1.Add a Contact")
    print("2.Update Contact ")
    print("3.Search number")
    print("4.Search email")
    print("5.Delete Contact")
    print("6.Exit")
    n=int(input("ENTER CHOICE :"))
    if n>6:
        print("ENTER VALID CHOICE")
    elif n==1:
        addmember()
    elif n==2:
        update()
    elif n==3:
        dispnumb()
    elif n==4:
        dispemail()
    elif n==5:
        delete()
    elif n==6:
        print("..EXIT..")
        exit()
    else:
        print("Invalid selection")
        print("")
    operations()        
operations()     