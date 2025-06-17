n=3
for i in range(n):
    for j in range(i,n-1):
        print(" ",end=" ")
    p=1
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    p=i
    for j in range(i):
        print(p,end=" ")
        p-=1
    print()
for i in range(n-2,-1,-1):
    for j in range(i,n-1):
        print(" ",end=" ")
    p=1
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    p=i
    for j in range(i):
        print(p,end=" ")
        p-=1
    print()

