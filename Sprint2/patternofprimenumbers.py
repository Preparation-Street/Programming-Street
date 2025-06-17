rows=3
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

for i in range(1,rows+1):
    current = 2
    prime=[]
    while len(prime)<i:
        if is_prime(current):
            prime.append(current)
        current+=1
    print(' '.join(map(str,prime)))
