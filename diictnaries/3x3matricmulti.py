# matrix1=[[1,2,3],[4,5,6], [7,8,9]]
# matrix2=[[7,8,9],[4,5,6],[1,2,3]]
matrix3= [[0,0,0],[0,0,0], [0,0,0]]
rows=int(input("enter the no of rows"))
cols=int(input("enter the no of coloumns"))
matrix1=[]
print("Enter array elements: ")
for i in range(rows):
    b=[]
    for j in range(cols):
        b.append(int(input()))
    matrix1.append(b)
for i in range(rows):
    for j in range(cols):
        print(matrix1[i][j],end=" ")
    print()
rows1=int(input("enter the no of rows"))
cols2=int(input("enter the no of coloumns"))
matrix2=[]
print("Enter array elements: ")
for i in range(rows1):
    d=[]
    for j in range(cols2):
        d.append(int(input()))
    matrix2.append(d)
for i in range(rows1):
    for j in range(cols2):
        print(matrix2[i][j],end=" ")
    print()

for i in range(rows):
   for j in range(cols2):
       for k in range(len(matrix2)):
           matrix3[i][j] += matrix1[i][k]*matrix2[k][j]
for r in matrix3:
    print(r)