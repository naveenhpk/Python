rows=int(input("enter the no of rows"))
cols=int(input("enter the no of coloumns"))
x=[]
print("Enter array elements: ")
for i in range(rows):
    b=[]
    for j in range(cols):
        b.append(int(input()))
    x.append(b)
for i in range(rows):
    for j in range(cols):
        print(x[i][j],end=" ")
    print()
matrix3= [[0,0,0],[0,0,0], [0,0,0]]
a=x[0][1]+x[0][2]+x[1][2]
b=x[1][0]+x[2][0]+x[2][1]
print("result")
if a==b:
    print("no change")
elif a>b:
    x[1][0]=x[2][0]=x[2][1]=0
    x[0][1]=x[0][2]=x[1][2]=1
else:
    x[1][0]=x[2][0]=x[2][1]=1
    x[0][1]=x[0][2]=x[1][2]=0
for i in range(rows):
    for j in range(cols):
        print(x[i][j],end=" ")
    print()
