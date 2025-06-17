n=3
for i in range(n):
    for j in range(i):
        print(" ",end="")
    ch = chr(ord('A')+n-i-1)
    for j in range(n-i):
        print(ch,end="")
    print()