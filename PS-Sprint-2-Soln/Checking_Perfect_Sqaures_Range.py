def check_Range(start , end):
    perfect_squares = []
    for num in range(start, end + 1):
        root = num ** 0.5
        if root.is_integer():
            perfect_squares.append(num)
    return perfect_squares

print(check_Range(1, 100))
print(check_Range(1,10))