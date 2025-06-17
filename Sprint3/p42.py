n=3
for i in range(n):
    for j in range(n+1):
        if (i+j)%2==0:
            print('A',end=" ")
        else:
            print("B",end=" ")
    print()