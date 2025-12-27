def sum_sqaures_even(n):
    total = 0
    for i in range(2, n+1, 2):
        total += i * i
    return total

print(sum_sqaures_even(10))
print(sum_sqaures_even(4))