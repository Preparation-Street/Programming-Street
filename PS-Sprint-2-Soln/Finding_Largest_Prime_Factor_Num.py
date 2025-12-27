def prime_factor(n):

    for i in range(2, n + 1):
        while n % i == 0:
            n = n // i
            largest_prime = i
    return largest_prime

print(prime_factor(28))