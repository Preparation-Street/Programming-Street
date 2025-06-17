array=[4,7,1,8,5]
min_arr=float('inf')
max_arr=-float('inf')
for i in range(len(array)):
    if array[i]>max_arr:
        max_arr=array[i]
    if array[i]<min_arr:
        min_arr=array[i]
print(max_arr)
print(min_arr)
