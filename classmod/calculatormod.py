def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
if __name__=='__main__':
    print("CHOICES")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    while True:
        n=int(input("Enter the choice :"))
        if n>5:
            print("choose a valid choice")
            continue
        elif n==5:
            print("..EXIT..")
            break
        a=float(input("Enter the first number"))
        b=float(input("Enter the second number"))
        if n==1:
            print("Sum=",add(a,b))
        elif n==2:
            print("differnce=",sub(a,b))
        elif n==3:
            print("Product=",mul(a,b))
        else:
            print("Divsion=",div(a,b))
    