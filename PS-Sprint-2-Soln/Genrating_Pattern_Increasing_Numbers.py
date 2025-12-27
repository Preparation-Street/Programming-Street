def gernating_pattern(n):
    matrix = []
    for i in range(n+1):
        row = []
        for j in range(1, i+1):
            row.append(j)
        matrix.append(row)
    return matrix
    
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))
print_matrix(gernating_pattern(3))