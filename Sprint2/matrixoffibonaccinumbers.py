size=3
a=0
b=1
matrix=[]
for i in range(size):
    row=[]
    for j in range(size):
        c=a+b
        a=b
        b=c
        row.append(a)
    matrix.append(row)
for row in matrix:
    print(' '.join(map(str,row)))
