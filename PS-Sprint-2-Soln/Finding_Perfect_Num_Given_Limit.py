def limit(n):
    for i in range(1,n):
        sum_divisors = 0
        for j in range(1, i):
            if i % j == 0:
                sum_divisors += j
        if sum_divisors == i:
            return i

print(limit(30))
