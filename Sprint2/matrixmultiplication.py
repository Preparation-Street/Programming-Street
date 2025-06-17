size=3
lst1=[]
for i in range(1,size+1):
    lst=[]
    for j in range(1,size+1):
        lst.append(i*j)
    lst1.append(lst)
for row in lst1:
    print(' '.join(map(str,row)))