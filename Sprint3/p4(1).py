n=3
for i in range(1,2*n):
    spaces=abs(n-i)
    stars=2*(n-spaces)-1
    print(" "*spaces+"*"*stars)