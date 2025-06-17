n=4
matrix=[]
for i in range(n):
    lst=[1]*(i+1)
    for j in range(1,i):
        lst[j]=matrix[i-1][j-1]+matrix[i-1][j]
    matrix.append(lst)

for row in matrix:
    print(" ".join(map(str,row)).center(n*2))

