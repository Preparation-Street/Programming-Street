def GCD(arr):
    for i in range(len(arr)):
        a = arr[i]
        for j in range(i + 1, len(arr)):
            b = arr[j]
            while b:
                a, b = b, a % b
            arr[j] = a
    return arr[1:]
print(GCD([24, 36, 60]))  # Outputs: [12, 12]