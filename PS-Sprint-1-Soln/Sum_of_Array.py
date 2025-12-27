def sum_Array(a):
    while len(a) > 1:
        a[0] = a[0] + a[1]
        a.pop(1)
    return a[0]

print(sum_Array([1, 2, 3, 4, 5]))  # Output: 15