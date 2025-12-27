def traingle(r):
    for i in range(r):
        print(' ' * (r - i), end='')
        val = 1
        for j in range(i + 1):
            print(val, end=' ')
            val = val * (i - j) // (j + 1)
        print()

traingle(4)