def sum_of_Series(n):
    total = 0 
    for i in range(1, n + 1):
        total += 1/i
    return total

print(sum_of_Series(4))  # Output: 2.283333333333333    