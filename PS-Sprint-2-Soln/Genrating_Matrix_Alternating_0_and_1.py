def genrating_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))
print_matrix(genrating_matrix(5))
print_matrix(genrating_matrix(3))