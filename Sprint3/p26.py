n=4
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print("A",end="")
        else:
            print("B",end="")
    print()