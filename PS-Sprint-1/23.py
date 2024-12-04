def fib(n):
    a=0
    b=1
    if n ==1:
        print(a)
    elif n == 2:    
        print(b, end = " ")
    else:    
        for i in range (2,n+1):
            c=a+b
            
            a=b
            b=c
        return c
n = int(input("ENter the No. : "))  
print(fib(n))          