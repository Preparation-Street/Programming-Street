n=3
col=4
p=1
for i in range(n):
    row=[]
    for j in range(col):
        row.append(p)
        p+=1
    if i%2!=0:
        row.reverse()
    print(*row)