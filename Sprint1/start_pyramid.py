n=5
for i in range(n+1):
    for j in range(i+1,n+1):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i+1,n+1):
        print(" ",end=" ")
    print()