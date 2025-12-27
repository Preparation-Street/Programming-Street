def sum_product(a,b):
    product = a * b
    total = 0
    for digit in str(product):
        total += int(digit)
    return total
print(sum_product(12, 13))  # Output: 6
print(sum_product(5, 7))    # Output: 5
print(sum_product(12,34))  # Output: 27