limit=int(input("Enter a number"))
a=0
b=1
if limit<=0:
    print("+ve integer")
elif limit==1:
    print(a)
else:
    print(a,b,end=" ")
    for i in range(2,limit):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
