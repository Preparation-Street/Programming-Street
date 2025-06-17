n=4
triangle=[]
for i in range(n):
    row=[1]*(i+1)
    for j in range(1,i):
        row[j]=triangle[i-1][j-1]+triangle[i-1][j]
    triangle.append(row)
print(triangle)
# for row in triangle:
#     print(" ".join(map(str,row)).center(n*2))

# for row in triangle:
#     print(" ".join(map(str,row)))
width=len(" ".join(map(str,triangle[-1])))
for row in triangle:
    row_str=" ".join(map(str,row))
    print(row_str.rjust(width))
