n=5
for i in range(n):
    if i==0 or i==n-1:
        for j in range(1,n//2+2):
            print(j,end="")
        for j in range(n//2,0,-1):
            print(j,end="")
    else:
        for j in range(n//2+1):
            print(j,end="")
        for j in range(n//2-1,-1,-1):
            print(j,end="")
    print()