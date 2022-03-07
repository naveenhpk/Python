rows=int(input("enter the no of rows"))
cols=int(input("enter the no of coloumns"))
a=[]
print("Enter array elements: ")
for i in range(rows):
    b=[]
    for j in range(cols):
        b.append(int(input()))
    a.append(b)
for i in range(rows):
    for j in range(cols):
        print(a[i][j],end=" ")
    print()
    
c=[]
print("Enter array elements: ")
for i in range(rows):
    d=[]
    for j in range(cols):
        d.append(int(input()))
    c.append(d)
for i in range(rows):
    for j in range(cols):
        print(c[i][j],end=" ")
    print()
if(a[i][j]==c[i][j]):
    print("same matrix")
else:
    print("not same")