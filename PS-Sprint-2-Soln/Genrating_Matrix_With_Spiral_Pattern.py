def pattern(n):
    # Create an n x n matrix filled with zeros
    matrix = [[0] * n for _ in range(n)]
    
    left, right = 0, n - 1
    top, bottom = 0, n - 1
    num = 1
    
    while left <= right and top <= bottom:
        # Fill the top row
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        # Fill the right column
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        if top <= bottom:
            # Fill the bottom row
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
        
        if left <= right:
            # Fill the left column
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    
    return matrix   

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))
print(print_matrix(pattern(4)))
print(print_matrix(pattern(3)))