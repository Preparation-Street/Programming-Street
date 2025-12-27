import random
def sqaure_matrix_random(n):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = random.randint(1,9)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))
print_matrix(sqaure_matrix_random(4))