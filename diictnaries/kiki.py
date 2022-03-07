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