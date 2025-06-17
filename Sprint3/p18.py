n=4
for i in range(n):
    if i==0 or i==n-1:
        for j in range(1,n+1):
            print(j,end="")
    else:
        print(1,end="")
        for j in range(n-2):
            print(" ",end="")
        print(1,end="")
    print()
