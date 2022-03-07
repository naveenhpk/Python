print("************ CALCULATOR*************")
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("     ")
def calculate():
    print("Mode of Operation")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    n=int(input("Enter the choice"))
    if n in (1,2,3,4):
        a=float(input("Enter the first number"))
        b=float(input("Enter the second number"))
        if n==1:
            print("Sum=",add(a,b))
        elif n==2:
            print("differnce=",sub(a,b))
        elif n==3:
            print("Product=",mul(a,b))
        elif n==4:
            print("Divsion=",div(a,b))
        else:
            print("what u mean")
    else:
        print("Invalid selection")
        print("")
        calculate()
calculate()
    