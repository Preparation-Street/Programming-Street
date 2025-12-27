def count_digits_greater(num, digit):
    count = 0
    # Use abs() to handle negative numbers like -572839
    num = abs(num)
    
    # Special case: if num is 0, the loop won't run, 
    # but 0 is a digit we might need to check.
    if num == 0:
        return 1 if 0 > digit else 0

    while num > 0:
        last_digit = num % 10
        if last_digit > digit:
            count += 1
        num //= 10
    return count

print(count_digits_greater(572839, 5))   # Output: 3
print(count_digits_greater(-572839, 5))  # Output: 3 (Now works!)