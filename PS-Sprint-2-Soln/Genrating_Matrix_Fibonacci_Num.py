def Matrix_Fibonacci(n):
    total_elements = n * n
    matrix = [[0] * n for _ in range(n)]
    a,b =1,1
    for i in range(n):
        for j in range(n):
            if total_elements >0:
                matrix[i][j] = a
                a,b = b,a+b
                total_elements -=1
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))

print_matrix(Matrix_Fibonacci(4))


