n=3
for i in range(n):
    print(" "*(n-i-1),end=" ")
    for j in range(1,i+2):
        print(j,end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
for i in range(n-2,-1,-1):
    print(" "*(n-i-1),end=" ")
    for j in range(1,i+2):
        print(j,end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
