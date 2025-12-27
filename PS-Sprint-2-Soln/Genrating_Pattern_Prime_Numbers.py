def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def pattern_prime(n):
    primes = []
    current_num = 2
    while len(primes) < n:
        if prime(current_num):
            primes.append(current_num)
        current_num += 1
    for i in range(1,n+1):
        row_primes = primes[:i]
        print(" ".join(str(x) for x in row_primes))  
    

pattern_prime(10)