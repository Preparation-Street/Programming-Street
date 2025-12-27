def digits_sum(n):
    """Returns the sum of the digits of a number n."""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print(digits_sum(1234))  # Output: 10