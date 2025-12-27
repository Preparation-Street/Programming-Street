def matrix_pattern(n):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i >=j:
                matrix[i][j] = 1
    return matrix   
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))

print_matrix(matrix_pattern(4))