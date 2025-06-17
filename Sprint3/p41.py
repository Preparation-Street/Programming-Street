n=3
val=1
mat=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(val)
        val+=1
    if i%2==1:
        row.reverse()
    mat.append(row)
for row in mat:
    print(*row)