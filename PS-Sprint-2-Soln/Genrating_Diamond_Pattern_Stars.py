def pattern(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))
    for i in range(n - 1):
        print(' ' * (i + 1) + '* ' * (n - i - 1))

print(pattern(5))