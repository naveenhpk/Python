f = open(r"D:\DOCS\python\filesmod\employee.txt","r")
def add(w):
    f = open(r"D:\DOCS\python\filesmod\employee.txt","w")
    for i,j in w.items():
        f.write(str(i)+"."+str(j)+"\n")
    f.close()

def display():
    f = open(r"D:\DOCS\python\filesmod\employee.txt","r")
    a = f.read()
    r = ({int(i.split(".")[0]): ".".join(i.split(".")[1:]) for i in a.splitlines()})
    print(a)
    f.close()

def update():
    id = int(input("Enter your id:"))
    name = input("Enter your name:")
    f = open(r"D:\DOCS\python\filesmod\employee.txt","r")
    b = f.read()
    print(b)
    r = ({int(i.split(".")[0]): ".".join(i.split(".")[1:]) for i in b.splitlines()})
    r[id]=name
    print(r)
    f.close()
    print("Employee details added")
    add(r)

def delete():
    id = int(input("Enter your id:"))
    f = open(r"D:\DOCS\python\filesmod\employee.txt","r")
    b = f.read()
    r = ({int(i.split(".")[0]): ".".join(i.split(".")[1:]) for i in b.splitlines()})
    del r[id]
    print("deleted")
    add(r)

while True:
    print("1.Display\n2.Add or Update\n3.Delete\n4.Exit :")
    choice = input("Enter your choice:")
    if choice =='1':
        display()
    elif choice =='2':
        update()
    elif choice=='3':
        delete()
    elif choice=='4':
        break
    else:
        print("Invalid choice")

f.close()