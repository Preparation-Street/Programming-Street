import random
n=3
matrix=[]
for i in range(n):
    lst=[]
    for j in range(n):
        val=random.randint(1,9)
        lst.append(val)
    matrix.append(lst)
for row in matrix:
    print(' '.join(map(str,row)))
