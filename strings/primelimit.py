a=int(input("Enter a limit"))
b=0
print("prime numbers in between ",a,"is:")
for i in range(1,a+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)
          