r=int(input("Enter the row number: "))
c=int(input("Enter the column number: "))
a=[]
lower=0
upper=0
print("Enter the elements: ")
for i in range(r):
    b=[]
    for j in range(c):
        b.append(int(input()))
    a.append(b)
for i in range(r):
    for j in range(c):
        print(a[i][j],end=" ")
    print()
print("sum of lower diagonal elements")
for i in range(r):
    for j in range(c):
        if (i>j):
            lower=lower+a[i][j]
print(lower)
print(" sum of upper diagonal elements")
for i in range(r):
    for j in range(c):
        if (i<j):
            upper=upper+a[i][j]
print(upper)       
for i in range(r):
    for j in range(c):
    	if upper<lower:
    		if i==j:
    			print("no change")
    		elif i<j:
    			a[i][j]=0
    		else:
    			a[i][j]=1    
    	else:
    		if i<j:
    			a[i][j]=1
    		else:
    			a[i][j]=0 
for i in range(r):
    for j in range(c):
        print(a[i][j],end=" ")
    print()