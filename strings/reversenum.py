a=int(input("enter the numbers"))
temp=a
reverse=0
while(temp>0):
    reminder=temp%10
    reverse=(reverse*10)+reminder
    temp=temp//10
print("reverse of",a,"is",reverse)