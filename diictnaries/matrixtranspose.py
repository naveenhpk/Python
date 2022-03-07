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
print("Transpose")
for i in range(rows):
    for j in range(cols):
       print(a[j][i],end=" ")
    print()