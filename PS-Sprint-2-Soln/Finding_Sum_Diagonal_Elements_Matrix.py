def sum_diaogonal(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]  # Primary diagonal
        total += matrix[i][n - 1 - i]  # Secondary diagonal
    if n % 2 == 1:
        total -= matrix[n // 2][n // 2]  # Subtract the middle element if n is odd
    return total
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
print(sum_diaogonal(matrix))  # Output: 30
