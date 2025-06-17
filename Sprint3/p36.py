n=3
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print("X",end="")
        else:
            print("0",end="")
    print()