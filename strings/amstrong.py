a=int(input("Enter a number"))
b=a
amst=0
while (a!=0):
    c=a%10
    amst=(c**3)+amst
    a=a//10
print("amstrong=",amst)
if(b==amst):
    print(b," is an amstrong number")
else:
    print(b," is not an amstrong number")
