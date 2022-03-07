a=int(input('Enter a number'))
if (a%2)==0:
    if (a%5)==0:
        print(a,"is divisible by both 2 and 5")
    else:
        print(a,"is only divisible by 2")
else:
    if (a%5)==0:
        print(a,"is  divisible  5")
    else:
        print(a,"is  divisible by 2 & 5") 
           