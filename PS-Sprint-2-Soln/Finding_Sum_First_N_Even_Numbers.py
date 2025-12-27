def sum_even(n):
    total = 0
    for i in range(n+1):
        total += 2 * i
    return total
print(sum_even(4))