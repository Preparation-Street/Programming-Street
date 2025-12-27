def matrix(n):
    result = []
    current_number = 0
    for i in range(n):
        row = []
        for j in range(n):

            print(current_number, end=" ")
            row.append(current_number, )
            current_number += 1
        print()
        # result.append(row)
    
    # return result
print(matrix(3))
print(matrix(4))