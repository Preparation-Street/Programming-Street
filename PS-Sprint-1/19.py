def prime(n):
    if n ==0 or n==1:
        return False
    for i in range (2, n):
        if (n%i) ==0:
            return False
    
    return True
def prime_inrange(a,b):
    prime_numbers = []
    for i in range(a,b+1):
        if prime(i):
            prime_numbers.append(i)
    return prime_numbers
a=1
b=24

print("Prime numbers between",a,"and",b,"are:",prime_inrange(a,b))
            