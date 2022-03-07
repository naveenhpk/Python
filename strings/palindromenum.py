a=int(input("Enter a number"))
reverse=0
temp=a
while (temp>0):
    reminder=temp%10
    reverse=(reverse*10)+reminder
    temp=temp//10
print("reverse of ",a,"is:",reverse)
if(reverse==a):
    print("it is a palindrome")
else:
    print("it is not a palindrome")
