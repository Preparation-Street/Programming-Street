matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst=[]
for row in matrix:
    largest=max(row)
    lst.append(largest)
print(lst)
