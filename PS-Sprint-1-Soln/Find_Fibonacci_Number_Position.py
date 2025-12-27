def postion(n):
    a = 0 
    b=1
    if n==0:
        return a
    else:
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return b
    
print(postion(5))