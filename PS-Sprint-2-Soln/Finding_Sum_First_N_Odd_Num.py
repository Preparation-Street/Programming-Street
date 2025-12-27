def sum_of_odd(n):
    total = 0 
    for i in range(1, n * 2, 2):
        total += i
    return total
print(sum_of_odd(5))  # Outputs: 25
print(sum_of_odd(10)) # Outputs: 100