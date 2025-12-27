def Sum_Fibonnaci(n):
    a, b = 1, 1
    sum_fib = 0
    for _ in range(n):
        sum_fib += a
        a, b = b, a + b
    return sum_fib

print(Sum_Fibonnaci(5))  # Output: 12