size=4
for i in range(size):
    for j in range(size):
        if i==j or i>j:
            print(1,end=" ")
        elif i<j:
            print(0,end=" ")
    print()
