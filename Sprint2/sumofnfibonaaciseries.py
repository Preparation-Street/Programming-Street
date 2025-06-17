n=5
lst=[]
a,b=0,1
for i in range(n):
    c=a+b
    a=b
    b=c
    lst.append(a)
print(sum(lst))