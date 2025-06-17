size=5
n=size//2
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
for i in range(n-1,-1,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()