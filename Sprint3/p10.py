n=3
for i in range(n):
    for j in range(i,n-1):
        print(" ",end="")
    p=i+1
    for j in range(i+1):
        print(p,end="")
        p+=1
    q=p-2
    for j in range(i):
        print(q,end="")
        q-=1
    print()
