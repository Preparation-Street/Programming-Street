import random
rows=2
columns=3
matrix=[]
for i in range(rows):
    row=[]
    for j in range(columns):
        row.append(random.randint(1,10))
    matrix.append(row)
for row in matrix:
    print(' '.join(map(str,row)))