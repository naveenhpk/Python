matrix3= [[0,0,0],[0,0,0], [0,0,0]]
rows=int(input("enter the no of rows"))
cols=int(input("enter the no of coloumns"))
matrix1=[]
print("Enter matrix 1 elements: ")
for i in range(rows):
    b=[]
    for j in range(cols):
        b.append(int(input()))
    matrix1.append(b)
for i in range(rows):
    for j in range(cols):
        print(matrix1[i][j],end=" ")
    print()
matrix2=[]
print("Enter matrix 2 elements: ")
for i in range(rows):
    d=[]
    for j in range(cols):
        d.append(int(input()))
    matrix2.append(d)
for i in range(rows):
    for j in range(cols):
        print(matrix2[i][j],end=" ")
    print()
print("Sum Of 2 Matrix")
for i in range(rows):
   for j in range(cols):
           matrix3[i][j]= matrix1[i][j]+matrix2[i][j]
for r in matrix3:
    print(r)