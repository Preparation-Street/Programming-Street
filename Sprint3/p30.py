n=5
for i in range(n):
    print(" "*i+"* "*(n-i))
for i in range(1,n):
    print(" "*(n-i-1)+"* "*(i+1))