def matrix(n):
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        print('\t'.join(map(str, row)))

print(matrix(5))
print(matrix(3))
