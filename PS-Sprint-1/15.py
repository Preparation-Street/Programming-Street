array = [3, 1, 4, 1, 5, 9]  
n = len(array)
for i in range (0, n):
    for j in range (i+1, n):
        if array[i]>array[j]:
            array[i], array[j] = array[j], array[i]
print (array)    