position=5
a,b=0,1
print(a,b,end=" ")
for i in range(position):
    c=a+b
    a=b
    b=c
    print(c,end=" ")

