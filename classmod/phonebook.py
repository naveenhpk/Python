data={}
def addmember():
    details={}
    name=input("NAME :")
    data[name]=details
    phone=[]
    ph=int(input("Enter  how many numbers  : "))  
    print("enter the numbers")
    for i in range(ph): 
        num=int(input()) 
        phone.append(num)
    details['Phone']=phone  
    email=[]   
    em=int(input("Enter  how many email : "))  
    print("enter the emails")
    for i in range(em): 
        emid=(input()) 
        email.append(emid)
    details['Email']=email
    print(data)
def display():
    print("----Search----")
    i=input("Enter the name")
    if i in data:
        print(i,":",data(i))
    else:
        print("hdhcf")
addmember()
display()



# def update():


