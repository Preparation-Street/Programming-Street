def num(n):
    while n >= 10:
        sum_digits = 0
        for i in range(len(str(n))):
            digit = n % 10
            sum_digits += digit
            n = n // 10
        n = sum_digits
    return n
print(num(38))
print(num(1234))
print(num(9875))