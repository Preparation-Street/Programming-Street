matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sumval=0
n=len(matrix[0])
m=len(matrix)
for i in range(n):
    sumval+=matrix[i][i]
print(sumval)