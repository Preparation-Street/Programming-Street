n=3
p=65
for i in range(n):
    print(" "*(n-i),end="")
    for j in range(2*i+1):
        print(chr(p),end="")
        p+=1
    print()